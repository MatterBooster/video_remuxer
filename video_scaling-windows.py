import time
import subprocess
import os
import argparse
import json

encoding_skip="0"
encoding_method="2"

################################################################################
####              Parse --testing for devoloper mode                        ####
################################################################################

command = 'cls'
subprocess.run(command, shell=True)

parser = argparse.ArgumentParser()
parser.add_argument('--testing', action='store_true', help='Enable testing mode')
args = parser.parse_args()
testing = 0
if args.testing:
    testing = "1"
    print('Developer mode activated')
    time.sleep(2)


command = 'cls'
subprocess.run(command, shell=True)

print("This script is for the following Fileformats:")
print(".mp4 .mov .avi .mkv .webm .mpeg .mpg\n")

time.sleep(5)
command = 'cls'
subprocess.run(command, shell=True)

################################################################################
####                  Function for printing GPU details                     ####
################################################################################

def get_gpu_details():
    command = 'wmic path win32_VideoController get name'
    output = subprocess.check_output(command).decode('utf-8').strip()
    return(output)

################################################################################
####                  Function for checking for GPU Vendor                  ####
################################################################################

def extract_variable_word(gpu_name):
    words = gpu_name.split()
    AMD_word = [word for word in words if "AMD" or "NVIDIA" or "Intel" in word]
    return AMD_word[0] if AMD_word else ""

def check_gpu_vendor(encoding_skip,encoding_method):
    data = get_gpu_details()

    lines = data.split('\n')  # Split the data into lines
    lines = [line.strip() for line in lines]  # Remove leading/trailing whitespace
    lines = lines[1:]  # Remove "Name" line

    gpu_variables = {}
    vendor_variables = {}
    for i, line in enumerate(lines):
        gpu_variable_name = f'gpu{i}'
        vendor_variable_name = f'vendor{i}'
        gpu_variables[gpu_variable_name] = line
        vendor_variables[vendor_variable_name] = extract_variable_word(line)

    print("You have the following GPUs installed:\n")
    for variable_name, value in gpu_variables.items():
        print(value)
        print()

    vendor0="0"
    vendor1="0"
    vendor2="0"

    for variable_name, value in vendor_variables.items():
        if testing=="1":
            print(f'{variable_name}: {value}')
        if vendor0=="0":
            vendor0=value
        if vendor0!=value and vendor1=="0":
            vendor1=value
        if vendor0!=value and vendor1!=value and vendor2=="0":
            vendor2=value
        if value=="0" and vendor0=="0" and vendor1=="0" and vendor2=="0":
            print("No gpu detected, will use Cpu encoding.")
            encoding_method = "2"
            encoding_skip="1"
            input("Press Enter to continue")
    gpu=0
    if vendor0=="0":
        encoding_skip=1
        encoding_method=1
    if encoding_skip!="1":
        while True:
            if vendor1!="0":
                if vendor2!="0":
                    print("You have the following GPUs installed:",vendor0,",",vendor1,",",vendor2)
                    gpu = input("which of these do you want: ")
                    if gpu=="AMD" or gpu=="NVIDIA" or gpu=="Intel":
                        break
                    else:
                        print("this is not an valid input")
                        continue
                print("You have the following GPUs installed:",vendor0,",",vendor1)
                gpu = input("which of these do you want: ")
                if gpu==vendor0 or gpu==vendor1:
                    break
                else:
                    print("this is not an valid input")
                    continue
            gpu=vendor0
            break
    return(gpu,encoding_skip,encoding_method)

################################################################################
####              Function for checking for the right extension             ####
################################################################################

def compatibility_check(extension):
    if extension==".mp4" or extension==".MP4" or extension==".Mp4" or extension==".MOV" or extension==".Mov" or extension==".mov" or extension==".AVI" or extension==".Avi" or extension==".avi" or extension==".MKV" or extension==".Mkv" or extension==".mkv" or extension==".flv" or extension==".wmv" or extension==".WEBM" or extension==".Webm" or extension==".webm" or extension==".MPEG" or extension==".Mpeg" or extension==".mpeg" or extension==".MPG" or extension==".Mpg" or extension==".mpg" or extension==".3gp" or extension==".m4v":
        command = 'cls'
        subprocess.run(command, shell=True) 
        return 1
    else:
        return 0

################################################################################
####                  Function for checking for audio_codec                 ####
################################################################################

def get_audio_codec(file_path):
    command = ['ffprobe', '-v', 'error', '-select_streams', 'a:0', '-show_entries', 'stream=codec_name', '-of', 'json', file_path]
    output = subprocess.check_output(command)
    data = json.loads(output)
    audio_codec = data['streams'][0]['codec_name']
    return audio_codec

################################################################################
####                        Testing the GPUs                                ####
################################################################################

gpu,encoding_skip,encoding_method=check_gpu_vendor(encoding_skip,encoding_method)

time.sleep(5)
command = 'cls'
subprocess.run(command, shell=True)

################################################################################
####                      Setting the Video Codec                           ####
################################################################################
if encoding_skip!="1":      #if no gpu is detected will use CPU automatically
    print("Choose your preferred video encoding method:\n")
    print("1. Software (CPU) encoding")
    print("2. GPU h264 encoding (Empfohlen)")
    print("3. GPU h265 encoding")
    print("4. GPU AV1 encoding\n")

    help = 0
    while True:
        encoding_method = input("Press enter to use the standard method (GPU h264) or enter the number corresponding to your choice: ")
    ##########################     HELP-Section1     ################################
        if help=="1":
            command = 'cls'
            subprocess.run(command, shell=True)
            print("Choose your preferred video encoding method:\n")
            print("1. Software (CPU) encoding")
            print("2. GPU h264 encoding (Empfohlen)")
            print("3. GPU h265 encoding")
            print("4. GPU AV1 encoding\n")
            help="0"
    ##########################     No Input     ################################
        if encoding_method == "":
            encoding_method = "2"
    ##########################     Right Input     ################################
        if encoding_method == "1" or encoding_method == "2" or encoding_method == "3" or encoding_method == "4":
            break
    ##########################     End Input     ################################
        if encoding_method == 'c' or encoding_method == 'e' or encoding_method == 'exit' or encoding_method == 'beenden' or encoding_method == 'end' or encoding_method == 'schließen':
            print("The Program will Terminate in:")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            exit()
    ##########################     HELP-Section2     ################################
        if encoding_method == 'h' or encoding_method == 'help' or encoding_method == 'hilfe':
            help="1"
            continue
    ##########################     Loop Tips     ################################
        print("This number is not specified please put in one of the Options or type 'help' or 'h' to see the options again")
        print("Type 'c', 'e' or 'exit' to end the program\n")

    if testing=="1":
        command = 'cls'
        subprocess.run(command, shell=True)
        print("encoding_method: ",encoding_method)
        print("gpu: ",gpu)
        input("Press Enter to continue...")
    
################################################################################
####                     Setting the Resolution                             ####
################################################################################
    
command = 'cls'
subprocess.run(command, shell=True)

resolution = input("Enter the resolution (Standard: 1920x1080): ")
if resolution == "":
    resolution = "1920x1080"
width, height = resolution.split('x')
resolution0 = "scale=" + width + ':' + height
if testing=="1":
    print("resolution",resolution)
    input("Press Enter to continue...")
    
################################################################################
####                     Setting the Extension                              ####
################################################################################

command = 'cls'
subprocess.run(command, shell=True)

extension1 = "0"
print("These are the compatible file extensions: .mp4, .mov, .avi, .mkv, .flv, .wmv, .webm, .mpeg, .mpg, .3gp, .m4v")
extension0 = input("Enter the file extension in to which you want to convert (standard: original): ")
if extension0 == "":
    extension1 = "1"
    
################################################################################
####                     Setting the Audiocodec                             ####
################################################################################

command = 'cls'
subprocess.run(command, shell=True)

audio_codec1 = "0"
print("These are the most used codec: aac, mp3 (old), libopus, flac, libvorbis")
audio_codec = input("Enter the audio codec in to which you want to convert (standard: original): ")
if audio_codec == "":
    audio_codec1 = "1"
if audio_codec:
    audio_codec= '-c:a ' + audio_codec

################################################################################
####                       Setting the Paths                                ####
################################################################################

command = 'cls'
subprocess.run(command, shell=True)
input_folder = input("Enter the input folder path: ")

command = 'cls'
subprocess.run(command, shell=True)

output_folder = input("Enter the output folder path: ")

##########################     Input Folder     ################################
command = 'cls'
subprocess.run(command, shell=True)
while True:
    command = 'cls'
    subprocess.run(command, shell=True)
    answer = input("Is the input folder '" + input_folder + "' correct? (y/n) ")

    if answer=="y" or answer=="Y" or answer=="j" or answer=="J" or answer=="Yes" or answer=="yes" or answer=="Ja" or answer=="ja":
        print("\nOK, than we will go with", input_folder, "as the input Folder.\n\n")
        time.sleep(1)
        command = 'cls'
        subprocess.run(command, shell=True)
        break
    else:
        input_folder = input("Then enter the new input folder path: ")
##########################     Output Folder     ################################
while True:
    command = 'cls'
    subprocess.run(command, shell=True) 
    
    answer = input("Is the output folder '" + output_folder + "' correct? (y/n) ")

    if answer=="y" or answer=="Y" or answer=="j" or answer=="J" or answer=="Yes" or answer=="yes" or answer=="Ja" or answer=="ja":
        print("\nOK, than we will go with", output_folder, "as the output Folder.\n\n")
        time.sleep(1)
        command = 'cls'
        subprocess.run(command, shell=True)
        break
    else:
        output_folder = input("Then enter the new output folder path: ")

################################################################################
####                       Checking the Files                               ####
################################################################################

for filename in os.listdir(input_folder):
    name, extension = os.path.splitext(filename)
    if compatibility_check(extension)==1:
        output_file = name + '_' + resolution + '.mp4'
        command = 'cls'
        subprocess.run(command, shell=True)
        print("Your video:",filename,"will be converted to",output_file,".mp4\n")
        time.sleep(2)
################################################################################
####                        Setting the videocodec                          ####
################################################################################
        if encoding_method=="1":
            if testing=="1":
                print("encoding_method: ",encoding_method)
                input("Press Enter to continue...")
            codec="-c:v libx264"
        else:
##########################     H264     ################################
            if encoding_method=="2":
                if testing=="1":
                    print("encoding_method: ",encoding_method)
                    input("Press Enter to continue...")
                if gpu=="NVIDIA":
                    if testing=="1":
                        print("gpu: ",gpu)
                        input("Press Enter to continue...")
                    codec="-c:v h264_nvenc"
                if gpu=="AMD":
                    if testing==1:
                        print("gpu: ",gpu)
                        input("Press Enter to continue...")
                    codec="-c:v h264_amf"
                if gpu=="Intel":
                    if testing==1:
                        print("gpu: ",gpu)
                        input("Press Enter to continue...")
                    codec="-hwaccel qsv -c:v h264_qsv"
            else:
##########################     H265/HVEC     ################################
                if encoding_method=="3":
                    if testing=="1":
                        print("encoding_method: ",encoding_method)
                        input("Press Enter to continue...")
                    if gpu=="NVIDIA":
                        if testing=="1":
                            print("gpu: ",gpu)
                            input("Press Enter to continue...")
                        codec="-c:v hevc_nvenc"
                    if gpu=="AMD":
                        if testing=="1":
                            print("gpu: ",gpu)
                            input("Press Enter to continue...")
                        codec="-c:v hevc_amf"
                    if gpu=="Intel":
                        if testing=="1":
                            print("gpu: ",gpu)
                            input("Press Enter to continue...")
                        codec="-hwaccel qsv -c:v hevc_qsv"
                else:
##########################     AV1     ################################
                    if encoding_method=="4":
                        if testing=="1":
                            print("encoding_method: ",encoding_method)
                            input("Press Enter to continue...")
                        if gpu=="NVIDIA":
                            if testing=="1":
                                print("gpu: ",gpu)
                                input("Press Enter to continue...")
                            codec="-c:v av1_nvenc"
                        if gpu=="AMD":
                            if testing=="1":
                                print("gpu: ",gpu)
                                input("Press Enter to continue...")
                            codec="-c:v av1_amf"
                        if gpu=="Intel":
                            if testing=="1":
                                print("gpu: ",gpu)
                                input("Press Enter to continue...")
                            codec="-hwaccel qsv -c:v av1_qsv"
################################################################################
####                Getting the varibles for ffmpeg                         ####
################################################################################
##########################     input_file     ################################
        input_file = input_folder + '\\' + filename
        if testing=="1":
            print("input_file: ",input_file)
            input("Press Enter to continue...")
##########################    audio_codec     ################################
        if audio_codec1=="1":
            audio_codec = "" #get_audio_codec(input_file)
        if testing=="1":
            print("audio_codec: ",audio_codec)
            input("Press Enter to continue...")
##########################    output_file     ################################
        if extension1=="0":
            output_file = output_folder + '\\' + name + '_' + resolution + extension0
        if extension1=="1":
            output_file = output_folder + '\\' + name + '_' + resolution + extension
################################################################################
####                                Command                                 ####
################################################################################
        if testing=="1":
            print("command: ffmpeg -i",input_file,"-vf",resolution0,codec,"-crf 23 -b:v 0 -c:a",audio_codec,"-b:a 192k",output_file)
            input("Press Enter to continue...")
        command = f"ffmpeg -i {input_file} -vf {resolution0} {codec} -crf 23 -b:v 0 {audio_codec} -b:a 192k {output_file}"
        subprocess.run(command, shell=True)
        time.sleep(3)
##########################     AV1     ################################
    else:
        command = 'cls'
        subprocess.run(command, shell=True)
        print("The file extension", extension,"of the file", filename, "is not supported.\n")
        time.sleep(3)
################################################################################
####                                Ending                                  ####
################################################################################
print("Batch processing completed.")
print("The Program will Terminate in:")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
command = 'cls'
subprocess.run(command, shell=True)
time.sleep(1)
print(output_folder)
exit()
