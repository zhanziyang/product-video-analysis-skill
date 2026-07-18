# FFmpeg Workflow

## Metadata

```bash
ffprobe -v error -show_streams -show_format -of json video.mp4
```

## Regular frame sampling

```bash
ffmpeg -i video.mp4 -vf "fps=2,scale=1280:-2" frames/%05d.jpg
```

## Scene-change candidates

```bash
ffmpeg -i video.mp4   -vf "select='gt(scene,0.30)',showinfo,scale=1280:-2"   -vsync vfr scene/%05d.jpg
```

Scene detection is only a starting point. Product videos often change states inside one shot, so add dense sampling around UI actions, text replacements, morphs, and camera transitions.

## Audio extraction

```bash
ffmpeg -i video.mp4 -vn -ac 1 -ar 22050 -c:a pcm_s16le audio.wav
```

## PDF render inspection

Use the host PDF skill or Poppler:

```bash
pdftoppm -png -r 120 report.pdf rendered/page
```

Inspect all pages, not only the cover and a representative middle page.
