#first make a filder in your Newly created Repository. My folder name is WALLPAPER
Folder = "WALLPAPER"

#then rename all images to the pattern of 'wallpaper (13)'.
#On windows you can easily do this using F12. Select all images and press F12. Then rename any one file to the name like 'wallpaper'.
#all images will be renamed. note the last image name would be the number of files in the folder. In my case, 511.
TotalIMG = 512 #1 more bcs range is just upto this and not including this

#then upload all images into the folder in github. At a time you can only upload 100 images.

#then run the script in your pc and then upload the Readme file to the repo.

with open("README2.md","w") as f:
    for i in range(1,TotalIMG):
        f.write(f'<img src="WALLPAPER/wallpaper ({i}).jpg" alt="{i}"/> <br>')


#Finally, Edit the Readme file as you wish

#Thanks. By @lemondiee
