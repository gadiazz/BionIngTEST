# -*- coding: utf-8 -*-
import pygame
pygame.init()
joyInit = pygame.joystick.init()

import socket
valorBoton = 0
valorReal = 0
#create socket
def sendCommand1(valorToSend):
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_ip = "192.168.1.106"
    client_port = 1234
    tosend = str(valorToSend)
    client_socket.connect((client_ip,client_port))
    #t.sleep(0.005)
    client_socket.send(bytes(tosend, 'utf-8'))
    #responsee = client_socket.recv(4*1024)
    #print("Respuesta: ", responsee.decode())
    #t.sleep(0.005)
    client_socket.close()

class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 25)

    def tprint(self, screen, text):
        text_bitmap = self.font.render(text, True, (0, 0, 0))
        screen.blit(text_bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

#joyDevices = pygame.joystick.get_count()
#print(type(joyInit), type(joyDevices))
#print("Init Joysticks: ", joyInit, "\nJoysticks Devices: ", joyDevices)
screen = pygame.display.set_mode((700, 700))
screen.fill((255, 255, 255))
pygame.display.set_caption("Joystick example")
# Used to manage how fast the screen updates.
clock = pygame.time.Clock()
text_print = TextPrint()
joysticksObjects = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print("Joysticks Objects: ", joysticksObjects)

PS3Controller_1 = pygame.joystick.Joystick(pygame.joystick.get_count() - 1)
print("Joysticks PS3Controller_1: ", PS3Controller_1)
PS3Controller_1.init

if PS3Controller_1.init:
    print("PS3Controller_1 Initialize", "| Battery POWER: ",PS3Controller_1.get_power_level(),
          "| Name: ", PS3Controller_1.get_name(), "\n| Num axes: ", PS3Controller_1.get_numaxes(),
          "| Num Buttons: ",PS3Controller_1.get_numbuttons() )
else:
    print("PS3Controller_1 !NO Initialize¡")
joysticks = {}
windowSize = (350,500)

def main():
    # Set the width and height of the screen (width, height), and name the window.
    #screenT1 = pygame.display.set_mode(windowSize)
    #screenT2 = pygame.display.set_mode(windowSize)
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Joystick example")

    pygame.display.set_caption("Joystick example")

    # Used to manage how fast the screen updates.
    clock = pygame.time.Clock()

    # Get ready to print.
    text_print = TextPrint()

    # This dict can be left as-is, since pygame will generate a
    # pygame.JOYDEVICEADDED event for every joystick connected
    # at the start of the program.
    joysticks = {}

    done = False
    while not done:
        # Event processing step.
        # Possible joystick events: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
                if event.button == 0:
                    valorBoton = 1
                    joystick = joysticks[event.instance_id]
                    if joystick.rumble(0, 0.7, 500):
                        print(f"Rumble effect played on joystick {event.instance_id}")
                        
             

            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")
                #client_socket.connect((client_ip,client_port))
                #client_socket.send(b"Hola saludos desde: CLIENTE[0]")
                #responsee = client_socket.recv(1024)
                #print("Respuesta: ", responsee.decode())
                #client_socket.close()

            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")

        # Drawing step
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.


        # Get count of joysticks.
        joystick_count = pygame.joystick.get_count()
        text_print.tprint(screen, f"Number of joysticks: {joystick_count}")
        text_print.indent()

        # For each joystick:
        for joystick in joysticks.values():
            #print(f" Joystick pos 0: {joysticks[0].get_name()} 0")
            #print(f" Joystick pos 1: {joysticks[1].get_name()} 1")
            #print(f"joystick: {joystick.get_name()} ")
            jid = joystick.get_instance_id()
            #if joystick.get_instance_id()== 0: screen = screenT1
            #if joystick.get_instance_id()== 1: screen = screenT2
            screen.fill((255, 255, 255))
            text_print.reset()

            text_print.tprint(screen, f"Joystick {jid}")
            text_print.indent()

            # Get the name from the OS for the controller/joystick.
            name = joystick.get_name()
            text_print.tprint(screen, f"Joystick name: {name}")

            guid = joystick.get_guid()
            text_print.tprint(screen, f"GUID: {guid}")

            power_level = joystick.get_power_level()
            text_print.tprint(screen, f"Joystick's power level: {power_level}")

            # Usually axis run in pairs, up/down for one, and left/right for
            # the other. Triggers count as axes.
            axes = joystick.get_numaxes()
            text_print.tprint(screen, f"Number of axes: {axes}")
            text_print.indent()

            for i in range(axes):
                axis = joystick.get_axis(i)
                text_print.tprint(screen, f"Axis {i} value: {axis:>6.3f}")

                if i == 1: 
                    if axis <=-0.5:
                    #axeEvent(i,axis,0,0,0)
                        sendCommand1("1")
                    if axis >=0.5 : 
                        sendCommand1("2")
                if i == 2: 
                    #axeEvent(i,axis,0,0,1)
                    if axis <=-0.5:
                    #axeEvent(i,axis,0,0,0)
                        sendCommand1("3")
                    if axis >=0.5 : 
                        sendCommand1("4")
                
            text_print.unindent()

            buttons = joystick.get_numbuttons()
            text_print.tprint(screen, f"Number of buttons: {buttons}")
            text_print.indent()

            for i in range(buttons):
                button = joystick.get_button(i)
                text_print.tprint(screen, f"Button {i:>2} value: {button}")
                if i == 0 and button != 0: 
                    #axeEvent(i,axis,0,0,4)
                    print("++PWM", button)
                    print("S: ","7")
                    sendCommand1("7")
                if i == 1 and button != 0:
                    #axeEvent(i,axis,0,0,5)
                    print("--PWM", button)
                    print("S: ","8")
                    sendCommand1("8")
                #client_socket.connect((client_ip,client_port))
                if i == 4 and button != 0: 
                    #axeEvent(i,axis,0,0,4)
                    print("GATILLO IZQ", button)
                    print("S: ","5")
                    sendCommand1("5")
                if i == 5 and button != 0:
                    #axeEvent(i,axis,0,0,5)
                    print("GATILLO DERECHO", button)
                    print("S: ","6")
                    sendCommand1("6")

                    
            text_print.unindent()

            hats = joystick.get_numhats()
            text_print.tprint(screen, f"Number of hats: {hats}")
            text_print.indent()

            # Hat position. All or nothing for direction, not a float like
            # get_axis(). Position is a tuple of int values (x, y).
            for i in range(hats):
                hat = joystick.get_hat(i)
                #text_print.tprint(screen, f"Hat {i} value: {str(hat)}")
            text_print.unindent()

            text_print.unindent()

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 30 frames per second.
        clock.tick(30)
    

if __name__ == "__main__":
    main()

    #client_socket.close()
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()