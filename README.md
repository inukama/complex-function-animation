# Complex Function Visualiser:

Python script to visualise complex function transformations.
To change the parameters, edit the variables near the top of the file.

# How To Use:

Change variables inside `visualiser.py` in order to vary paramters. Maybe I'll implement a GUI frontend in the future.

| Parameter | Description |
| --- | --- |
| `pw` | Amount of points used to represent each grid-line. Lower values (<100) result in choppier looking graphs, but perform better, and higher values will give you a smoother graph at the cost of performance. |
| `grid_w` | "Radius" or wingspan of the grid. The grid's width is double `grid_w` |
| `view_w` | Similar to grid_w -- wingspan of the viewport |
| `amt` | How many gridlines to draw. E.g. if `amt`=3, 3 horizontal lines and 3 vertical lines will form the grid. Using higher values lets you visualise more localised features of the graph, but high values (>300) will be significantly slower |
| `transform_caption` | Title of the graph. Enclose any LaTeX with $ (e.g. $\frac{1}{2}$) |
| `def transform(z)` | The transform function. This is the actual function we use to transform. Edit it to try different functions |
| `save_to_file` | If set to `True`, the program will not display and will instead save directly to `file_output` |
| `file_output` | The file to which the program renders and saves the result |
| `max_steps` | Choose the amount of frames in the animation. If the computation is expensive or you want a very high resolution, it might be worth tuning this down to the single digits. |
| `minp`/`maxp` | Fine tune the location of the grid by setting the bottom right hand corner (`minp`) and the top right hand corner (`maxp`). Both are in the format (x, y) |
| `viewmin`/`viewmax` | Fine tune the location of the viewing window. Same as `minp` and `maxp` |
|`fps`| Frames per second of output animation. Recommended to keep this low (e.g. 10fps. matplotlib will not display higher frame rates due to performance limitations.)|
|`major_interval`| Choose interval between differently coloured (major) lines|
|`major_lines`| True or False to choose whether or not to draw major lines |
|`col1`/`col2`| Colour (RGB) of the vertical and horizontal gridlines respectively|
|`majcol`| Colour of the major gridlines |
