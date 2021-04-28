
import time
import src.helpers


class application:
  
  def __init__(self, username="", app_name="pluto", application_runner_command="NaN"):
    
    if application_runner_command == "py-cli run application":
      
      self.app_name = app_name
      self.currentVersion = "1.0"
      
      # Checking that the username is valid or not
      if username == None or username == "":
        self.username = input("({})> Enter a username for the setup> ".format(self.app_name))
      else: self.username = username

      # Declaring the self object for helpers
      # to be used by all the features/methods
      self.HELPER = src.helpers.helpers()
      
      self.home()
    
  
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
      if (self.userCommand == "py-cli projects"):
        self.projectListingInterface()
      if (self.userCommand == "py-cli help"):
        print(
          self.getHelpCommandInterface())
      if (self.userCommand == "py-cli projects --add-project"):
        print(
          self.addNewProjectInterface())
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
        ~ Description of the project
        ~ GitHub Repository URL
        ~ Version release of the Project
        ~ Author Name
        ~ LICENSE of the Project
        ~ Project special-init command
    '''

  def projectListingInterface(self):
    pass
  
  
  def addNewProjectInterface(self):
    self.PROJECT_NAME = self.application_ask_command(
        "Enter the Name of your project")
    
    self.PROJECT_DESCRIPTION = self.application_ask_command(
        "Give your project a description")
    
    self.PROJECT_GITHUB_URL = self.application_ask_command(
        "Enter the GitHub URL of the project")
    
    self.PROJECT_VERSION = self.application_ask_command(
        "Initial Version of the Project")
    
    self.PROJECT_AUTHOR_NAME = self.application_ask_command(
        "Name of the Author")
    
    self.PROJECT_START_FILE = self.application_ask_command(
        "Base(Starting/Setup) file of the project")
    
    self.LICENSE_NAME = self.application_ask_command(
        "LICENSE of the Project")
    
    self.PROJECT_INIT_COMMAND = self.application_ask_command(
        "Create a special Init Command to run your project")
    
    self.PROJECT_DATA = [self.PROJECT_INIT_COMMAND,
                         self.PROJECT_GITHUB_URL,
                         self.PROJECT_NAME,
                         self.PROJECT_VERSION,
                         self.PROJECT_START_FILE,
                         self.PROJECT_AUTHOR_NAME]
    if (self.HELPER.checkForEmptyStringsInArray(self.PROJECT_DATA) == "HasEmptyString"):
      print('''
        ({}) Project \'{}\' was unable to be added to the application.
        Please re-run the command \'py-cli projects --add-project\'
        '''.format(
          self.app_name,
          self.PROJECT_NAME))
    else:
      print(
        '''
        Project ({}) added successfully. The new JSON Object for project
        is given below
        
        \"project_name\": [
          ...
          \"{}\": [
            \"name\": \"{}\",
            \"description\": \"{}\",
            \"github_url\": \"{}\",
            \"version\": \"{}\",
            \"author\": \"{}\",
            \"basefile\": \"{}\",
            \"license\": \"{}\",
            \"init\": \"{}\"
          ]
        ]
        
        '''.format(
          # highlighting the project name
          self.PROJECT_NAME,
          
          # showing project name as the name of the project
          self.PROJECT_NAME,
          
          # adding the project details
          self.PROJECT_NAME, self.PROJECT_DESCRIPTION,
          self.PROJECT_GITHUB_URL, self.PROJECT_VERSION,
          self.PROJECT_AUTHOR_NAME, self.PROJECT_START_FILE,
          self.LICENSE_NAME, self.PROJECT_INIT_COMMAND
        )
      )
      
      
  def application_ask_command(self, command_to_show):
    temp_input = input("({}) {}>".format(
      self.app_name, command_to_show
    ))
    return temp_input
