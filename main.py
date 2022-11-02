from util import blocksToStacks, CustomException

import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
  [
    sg.Input(key="-INPUT-"),
    sg.Button("Convert", key="-CONVERT-")
  ],
  [
    sg.Text("Stacks: ", key="-STACKS-"),
    sg.Text("Leftover: ", key="-LEFTOVER-")
  ],
  [
    sg.Text("", key="-ERROR-", text_color="red")
  ],
]

window = sg.Window('Minecraft - Blocks To Stacks Converter', layout)

numberInput = window["-ERROR-"]
stacksNo = window["-STACKS-"]
leftoverNo = window["-LEFTOVER-"]

def resetCounts():
  stacksNo.update("Stacks: ")
  leftoverNo.update("Leftover: ")

while True:
  event, values = window.read()
  
  if event == sg.WINDOW_CLOSED:
    break
  
  if event == '-CONVERT-':
    numberInput.update("")
    
    try:
      blocks = int(values["-INPUT-"])
      
      if abs(blocks) == 0:
        raise CustomException("Number must be greater than zero")
      
      returnData = blocksToStacks(blocks)
      
      stacksNo.update(f"Stacks: {returnData[0]}")
      leftoverNo.update(f"Leftover: {returnData[1]}") 
      
    except CustomException as e:
      numberInput.update(e)
      resetCounts()
      
    except ValueError:
      numberInput.update("Please enter a valid number")
      resetCounts()

       
print("Program closing...")  
window.close()