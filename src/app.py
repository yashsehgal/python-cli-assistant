
import time

class application:
  
  def __init__(self, username, app_name="pluto"):
    self.username = username
    self.app_name = app_name
    self.currentVersion = "1.0"
  
  # Creating a method Home, which will be the home(base) interface 
  # of the cli-application. This will have access of all the application
  # interface methods which will be executed according to the user's
  # command-inputs.
  def home(self):
    
    self.userCommand = ""
    
    # Running a while loop which will be running infinite times
    # until the user runs the exit command which is (py-cli exit)
    while self.userCommand != "py-cli exit":
      self.userCommand = input("({})>".format(self.username))
      if (self.userCommand == "py-cli start"):
        self.welcomeInterface()
      if (self.userCommand == "py-cli help"):
        print(
          self.getHelpCommandInterface())
      if (self.userCommand == "py-cli projects"):
        print(
          self.projectListingInterface())
      if (self.userCommand == "py-cli exit"):
        print(
          '''
          Exiting py-cli (PYTHON CLI ASSISTANT)...
          '''
        )
        time.sleep(1)
      
  def welcomeInterface(self):
    print("Hello ({}), I hope you are doing great today!!"
            .format(self.username))
    print("This is the (v{}) of the python-cli-assistant program"
            .format(self.currentVersion))
    print("Enter \'help\' to get started")
  
  def getHelpCommandInterface(self):
    return '''
    ************
    PY-CLI HELP INTERFACE - COMMANDS AND FEATURES ARE LISTED BELOW
    WITH PROPER EXPLANATION AND USAGE
    ************
    
    py-cli start      - To start the CLI application
    py-cli help       - To see the help/command list
    py-cli projects   - To see name of all the projects
      [--add-project]: To add new project details in the data
      
      1. Once you'll write 'py-cli projects --add-projects', the application
        will start a session of questions related to the project details.
      2. The flow of the questions will be:
        ~ Name of the Project
        ~ GitHub Repository URL
        ~ Version release of the Project
        ~ Author Name
        ~ LICENSE of the Project
        ~ Project special-init command
    '''

  def projectListingInterface(self):
    pass