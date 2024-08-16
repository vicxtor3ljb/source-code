import threading
import subprocess

def run_script(script_name):
	subprocess.run(["python", script_name])
	
if __name__ == "__main__":
	script1_thread = threading.Thread(target=run_script, args=("spaceinvaders1.py",))
	script2_thread = threading.Thread(target=run_script, args=("audioplayer.py",))
	script3_thread = threading.Thread(target=run_script, args=("text.py",))

	script1_thread.start()
	script2_thread.start()
	script3_thread.start()
	
	script1_thread.join()
	script2_thread.join()
	script3_thread.start()
	
	# print("Both scripts have finished executing")

