 #ffmpeg -ss 00:00:15 -i video3.mp4 -t 00:00:20 -vcodec copy -acodec copy trimed_video3.mp4
echo "======================================="
echo "Converting"
echo "======================================="
python3 video_predict.py
echo "======================================="
echo "Convertion Done"
echo "======================================="
ffmpeg -framerate 25 -pattern_type glob -i 'video_output/*.png' -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
echo "======================================="
echo "Video Created as out.mp4"
echo "======================================="
