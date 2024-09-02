import cv2
import pandas as pd
import argparse

def draw_bounding_boxes(video_path, csv_path, output_path, epochs):
    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Open the video
    cap = cv2.VideoCapture(video_path)

    # Get the video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Prepare to write the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    current_frame = 0
    box_color = (255, 3, 191)  # FF03BF in RGB
    text_color = (255, 255, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.6
    thickness = 1

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Filter the DataFrame for the current frame
        frame_data = df[df['Current Frame'] == current_frame]

        # Calculate the number of detections
        num_detections = len(frame_data)

        # Calculate the average surface area of the detections
        if num_detections > 0:
            areas = (frame_data['X Bound, Right'] - frame_data['X Bound, Left']) * (frame_data['Y Bound, Lower'] - frame_data['Y Bound, Upper'])
            avg_area = areas.mean()
        else:
            avg_area = 0

        # Draw bounding boxes and labels for each detection in the current frame
        for index, row in frame_data.iterrows():
            x_left = int(row['X Bound, Left'])
            y_upper = int(row['Y Bound, Upper'])
            x_right = int(row['X Bound, Right'])
            y_lower = int(row['Y Bound, Lower'])

            # Draw the rectangle on the frame
            cv2.rectangle(frame, (x_left, y_upper), (x_right, y_lower), box_color, 2)

            # Add the "Ophidurea" label above the bounding box
            label = "Ophidurea"
            label_size, _ = cv2.getTextSize(label, font, font_scale, thickness)
            label_y = max(y_upper - 10, label_size[1] + 10)
            cv2.putText(frame, label, (x_left, label_y), font, font_scale, text_color, thickness, cv2.LINE_AA)

        # Overlay text information
        text_y = 20

        # Display "GAEL YOLO 7" title
        gael_text = "GAEL"
        text_size, _ = cv2.getTextSize(gael_text, font, font_scale, thickness)
        text_x = int((width - text_size[0]) / 2)
        text_y += 60
        cv2.putText(frame, gael_text, (10, text_y), font, 2.5, text_color, thickness, cv2.LINE_AA)
        text_y += 60  # Increase the gap for subsequent lines of text

        # Display number of epochs
        cv2.putText(frame, f"{epochs} Epochs", (10, text_y), font, 1.5, text_color, thickness, cv2.LINE_AA)
        text_y += 40

        # Display frame number
        cv2.putText(frame, f'Frame: {current_frame + 1}/{total_frames}', (10, text_y), font, font_scale, text_color, thickness, cv2.LINE_AA)
        text_y += 20

        # Display number of sea stars (detections)
        cv2.putText(frame, f'Number of Brittle Stars (in Current Frame): {num_detections}', (10, text_y), font, font_scale, text_color, thickness, cv2.LINE_AA)
        text_y += 20

        # Display average surface area
        cv2.putText(frame, f'Avg Surface Area of Brittle Star: {avg_area:.2f} px^2', (10, text_y), font, font_scale, text_color, thickness, cv2.LINE_AA)

        # Write the frame with the bounding boxes
        out.write(frame)

        # Print progress
        print(f'Processing frame {current_frame + 1}/{total_frames}')
        current_frame += 1

    # Release the video objects
    cap.release()
    out.release()
    print(f'Overlay complete. Output saved to {output_path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Overlay bounding boxes from CSV on video.')
    parser.add_argument('--video', type=str, required=True, help='Path to the input video.')
    parser.add_argument('--csv', type=str, required=True, help='Path to the CSV file with bounding box data.')
    parser.add_argument('--output', type=str, required=True, help='Path to save the output video with bounding boxes.')
    parser.add_argument('--epochs', type=int, required=True, help='Number of epochs run in this training session CSV.')

    args = parser.parse_args()

    draw_bounding_boxes(args.video, args.csv, args.output, args.epochs)
