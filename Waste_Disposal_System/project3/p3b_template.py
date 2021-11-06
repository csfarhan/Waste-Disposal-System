import time
import random
import sys
sys.path.append('../')

from Common_Libraries.p3b_lib import *

import os
from Common_Libraries.repeating_timer_lib import repeating_timer

def update_sim():
    try:
        my_table.ping()
    except Exception as error_update_sim:
        print (error_update_sim)

### Constants
speed = 0.2 #Qbot's speed

### Initialize the QuanserSim Environment
my_table = servo_table()
arm = qarm()
arm.home()
bot = qbot(speed)

##---------------------------------------------------------------------------------------
## STUDENT CODE BEGINS
##---------------------------------------------------------------------------------------

##Created by Slader Moon

import random

#from start to pick up, line follow, only does once
def line_follow():
    print(bot.follow_line(0.1))
    lost_lines = 0
    while lost_lines < 2:
        lost_lines, velocity = bot.follow_line(0.1)
        bot.forward_velocity(velocity)
        time.sleep(0.2)

#Dispense bottle 1
def dispense_1():
    bott_ID = random.randint(1,6)   #Assign random number for bottle 1
    print(bott_ID)

    my_table.container_properties(bott_ID)   #Dispense bottle
    my_table.dispense_container()
    print(my_table.container_properties(bott_ID))
    bin_ID = my_table.container_properties(bott_ID)[2]   #Determine bin number
    time.sleep(2)
    my_table.rotate_table_angle(90)        #Rotate bottle to pickup location
    time.sleep(2)
    my_table.rotate_table_angle(90)
    time.sleep(2)
    my_table.rotate_table_angle(90)
    time.sleep(2)
    return bin_ID
        
#load bottle 1 to hopper
def load_container_1():      #Move qarm to pickup bottle and tranfer to hopper
    arm.rotate_elbow(-45)
    time.sleep(1)
    arm.rotate_shoulder(55)
    time.sleep(1)
    arm.control_gripper(45)
    time.sleep(1)
    arm.rotate_shoulder(-35)
    time.sleep(1)
    arm.rotate_base(-92)
    time.sleep(1)
    arm.rotate_shoulder(2)
    time.sleep(1)
    arm.rotate_elbow(33)
    time.sleep(1)
    arm.control_gripper(-25)
    time.sleep(1)
    arm.rotate_shoulder(-30)
    time.sleep(1)
    arm.home()
    time.sleep(2)
        
#Dispense bottle 2
def dispense_2():
    bott_ID_2 = random.randint(1,6)  #Assign random number for bottle 2
    print(bott_ID_2)

    my_table.container_properties(bott_ID_2)   #Dispense bottle
    my_table.dispense_container()
    print(my_table.container_properties(bott_ID_2))
    bin_ID_2 = my_table.container_properties(bott_ID_2)[2] #Determine bin number
    time.sleep(2)
    my_table.rotate_table_angle(90)     #Rotate bottle to pickup location
    time.sleep(2)
    my_table.rotate_table_angle(90)
    time.sleep(2)
    my_table.rotate_table_angle(90)
    time.sleep(2)
    return bin_ID_2
       
            
#load bottle 2 to hopper
def load_container_2():      #Move qarm to pickup bottle and tranfer to hopper
    arm.rotate_elbow(-45)
    time.sleep(1)
    arm.rotate_shoulder(55)
    time.sleep(1)
    arm.control_gripper(45)
    time.sleep(1)
    arm.rotate_shoulder(-35)
    time.sleep(1)
    arm.rotate_base(-82)       #Places second bottle beside first
    time.sleep(1)
    arm.rotate_shoulder(2)
    time.sleep(1)
    arm.rotate_elbow(25)
    time.sleep(1)
    arm.control_gripper(-25)
    time.sleep(1)
    arm.rotate_shoulder(-30)
    time.sleep(1)
    arm.home()
    time.sleep(2)
                
#Dispense bottle 3
def despense_3():
    bott_ID_3 = random.randint(1,6)   #Assign random number for bottle 2
    print(bott_ID_3)

    my_table.container_properties(bott_ID_3)     #Dispense bottle
    my_table.dispense_container()
    print(my_table.container_properties(bott_ID_3))
    bin_ID_3 = my_table.container_properties(bott_ID_3)[2]#Determine bin number
    time.sleep(2)
    my_table.rotate_table_angle(90)     #Rotate bottle to pickup location
    time.sleep(2)
    my_table.rotate_table_angle(90)
    time.sleep(2)
    my_table.rotate_table_angle(90)
    time.sleep(2)
    return bin_ID_3
                
#If bottle 3 is same bin as bottle 2 and bottle 1
#load bottle 3 to hopper
def load_container_3():
    arm.rotate_elbow(-45)       #Move qarm to pickup bottle and tranfer to hopper
    time.sleep(1)
    arm.rotate_shoulder(55)
    time.sleep(1)
    arm.control_gripper(45)
    time.sleep(1)
    arm.rotate_shoulder(-45)
    time.sleep(1)
    arm.rotate_base(-102)      #Places second bottle behind bottle 1
    time.sleep(1)
    arm.rotate_shoulder(5)
    time.sleep(1)
    arm.rotate_elbow(25)
    time.sleep(1)
    arm.control_gripper(-25)
    time.sleep(1)
    arm.rotate_shoulder(-30)
    time.sleep(1)
    arm.home()
    time.sleep(2)

#Drop off containers
def transfer_1(bin_ID):       
    if bin_ID == "Bin01":  
        #drop off container with sensor for Green
        time.sleep(1)
        bot.rotate(-140)
        time.sleep(2)
        print(bot.follow_line(0.1)[0])
        while bot.follow_line(0.1)[0] > 1:
            print(bot.follow_line(0.1)[0])
            bot.forward_velocity([0, 0.05])
            time.sleep(2)
        bot.stop()
        print("Calibrate complete")    #turn until line, more accurate
        time.sleep(1)
        bot.rotate(-22)
        time.sleep(1)
            
        bot.forward_time(3.8)

        #Detect correct color to ensure proper bin
        time.sleep(1)        
        bot.activate_color_sensor("Green")
        print(bot.read_green_color_sensor("Bin01", 0.6))
        print (sum(bot.read_green_color_sensor("Bin01", 0.6)) / 3)
        if (sum(bot.read_green_color_sensor("Bin01", 0.6)) / 3) > 4.5:
            
            #Dump bottle
            bot.activate_actuator()
            bot.dump()
            bot.deactivate_actuator()
            print("Container(s) dropped off to Bin01!")
            
            #Go around bend
            lost_lines = 0
            while lost_lines < 2:
                lost_lines, velocity = bot.follow_line(0.1)
                bot.forward_velocity(velocity)
     
            bot.deactivate_color_sensor()
    return bin_ID
                
    

def transfer_2(bin_ID):
    if bin_ID == "Bin02":  
        #drop off container with sensor for Blue
        time.sleep(1)
        bot.rotate(-140)
        time.sleep(2)
        print(bot.follow_line(0.1)[0])
        while bot.follow_line(0.1)[0] > 1:
            print(bot.follow_line(0.1)[0])
            bot.forward_velocity([0, 0.05])
            time.sleep(2)
        bot.stop()
        print("Calibrate complete")    #turn until line, more accurate
        time.sleep(1)
        bot.rotate(-22)
        time.sleep(1)

            
        bot.forward_time(5.8)
            
        #Detect correct color to ensure proper bin
        time.sleep(1)
        bot.activate_color_sensor("Blue")
        print(bot.read_blue_color_sensor("Bin02", 0.6))
        print (sum(bot.read_blue_color_sensor("Bin02", 0.6)) / 3)
        if (sum(bot.read_blue_color_sensor("Bin02", 0.6)) / 3) > 4.5:
                    
            #Dump bottle
            bot.activate_actuator()
            bot.dump()
            bot.deactivate_actuator()
            print("Container(s) dropped off to Bin02!")
            
            #Go around bend
            lost_lines = 0
            while lost_lines < 2:
                lost_lines, velocity = bot.follow_line(0.1)
                bot.forward_velocity(velocity)
     
            bot.deactivate_color_sensor()
    return bin_ID
        

def transfer_3(bin_ID):
    if bin_ID == "Bin03":  
        #drop off container with sensor for Red
        time.sleep(1)
        bot.rotate(-140)
        time.sleep(2)
        print(bot.follow_line(0.1)[0])
        while bot.follow_line(0.1)[0] > 1:
            print(bot.follow_line(0.1)[0])
            bot.forward_velocity([0, 0.05])
            time.sleep(2)
        bot.stop()
        print("Calibrate complete")     #turn until line, more accurate
        time.sleep(1)
        bot.rotate(-22)
        time.sleep(1)

        bot.forward_time(7.6)
        time.sleep(1)

        #Detect correct color to ensure proper bin
        bot.activate_color_sensor("Red")
        print(bot.read_red_color_sensor("Bin03", 0.6))
        print (sum(bot.read_red_color_sensor("Bin03", 0.6)) / 3)
        if (sum(bot.read_red_color_sensor("Bin03", 0.6)) / 3) > 4.5:
                    
            #Dump bottle
            bot.activate_actuator()
            bot.dump()
            bot.deactivate_actuator()
            print("Container(s) dropped off to Bin03!")
            
            #Go around bend
            lost_lines = 0
            while lost_lines < 2:
                lost_lines, velocity = bot.follow_line(0.1)
                bot.forward_velocity(velocity)
     
            bot.deactivate_color_sensor()
    return bin_ID
                
  
def transfer_4(bin_ID):
    if bin_ID =="Bin04":  
        #drop off container with sensor for White
        time.sleep(1)
        bot.rotate(-140)
        time.sleep(2)
        print(bot.follow_line(0.1)[0])
        while bot.follow_line(0.1)[0] > 1:
            print(bot.follow_line(0.1)[0])
            bot.forward_velocity([0, 0.05])
            time.sleep(2)
        bot.stop()
        print("Calibrate complete")    #turn until line, more accurate
        time.sleep(1)
        bot.rotate(-22)
        time.sleep(1)

            
        bot.forward_time(9.1)
        time.sleep(1)

        #Detect correct color to ensure proper bin
        bot.activate_color_sensor("Red")
        print(bot.read_red_color_sensor("Bin03", 0.6))
        print (sum(bot.read_red_color_sensor("Bin03", 0.6)) / 3)
        if (sum(bot.read_red_color_sensor("Bin03", 0.6)) / 3) > 4.5:
                    
            #Dump bottle
            bot.activate_actuator()
            bot.dump()
            bot.deactivate_actuator()
            print("Container(s) dropped off to Bin04!")
            
            #Go around bend
            lost_lines = 0
            while lost_lines < 2:
                lost_lines, velocity = bot.follow_line(0.1)
                bot.forward_velocity(velocity)
     
            bot.deactivate_color_sensor()
    return bin_ID
    


line_follow()

check = "y"
while check == "y":       #Repeat depending on user input
    bin_ID = dispense_1()
    load_container_1()
    bin_ID_2 = dispense_2()
    
    if bin_ID_2 == bin_ID:
        load_container_2()
        dispense_3()

        if bin_ID_2 == bin_ID and bin_ID_3 == bin_ID:
            load_container_3()
            
    transfer_1(bin_ID)
    transfer_2(bin_ID)
    transfer_3(bin_ID)
    transfer_4(bin_ID)

    check = input("To repeat process, Type y. To stop, Type n")
    if check != "y" or check != "n":
        check = input("Try again: To repeat process, Type y. To stop, Type n")
    








##---------------------------------------------------------------------------------------
## STUDENT CODE ENDS
##---------------------------------------------------------------------------------------
update_thread = repeating_timer(2,update_sim)
