from os import system as sst

print("Please run this as Super User")
partition = input(" What is the location of the partition[use lsblk to find out]? eg(sda6):  ")
sst("mount /dev/" + partition + " /mnt")
sst(" mount --bind /dev /mnt/dev && mount --bind /proc /mnt/proc && mount --bind /sys /mnt/sys && chroot /mnt ")
