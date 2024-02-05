#!/usr/bin/env python3

# df -H
# lscpu

import psutil
import time

def check_and_alert(input_CPU, input_DISK, input_MEMORY):
    
	while True:
		time.sleep(1)
		cpu_info 	= psutil.cpu_percent()
		partitions 	= psutil.disk_partitions()
		memory 		= psutil.virtual_memory()

		if cpu_info > input_CPU:
			print(f"Alert: current CPU {cpu_info} exceeds threshold {input_CPU}")
		if memory.percent > input_MEMORY:
			print(f"Alert: current memory usage {memory.percent} exceeds threshold {input_MEMORY}")
		for part in partitions:
			current_usage = psutil.disk_usage(part.mountpoint).percent
			if current_usage > input_DISK:
				print(f"Alert: {part.mountpoint} {current_usage} exceeds threshold {input_DISK}")

def main():

	try:
		input_CPU = float(input("Enter the threshold CPU: "))
		input_DISK  = float(input("Enter the threshold DISK: "))
		input_MEMORY  = float(input("Enter the threshold MEMORY: "))
		check_and_alert(input_CPU, input_DISK, input_MEMORY)
	except Exception as ex:
		print(ex)

if __name__ == "__main__":
	main()