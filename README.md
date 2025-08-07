# Python Learning Workspace

A comprehensive collection of Python learning materials, practice exercises, and projects covering fundamental concepts to intermediate-level programming. All content is organized in a logical, progressive structure for effective learning.

## 🚀 Quick Setup

### Virtual Environment Setup

Before starting, create a virtual environment to manage your Python dependencies:

```bash
# Create virtual environment
py -m venv python_learning_env

# Activate (Windows)
python_learning_env\Scripts\activate

# Activate (Linux/Mac)
source python_learning_env/bin/activate

# Install dependencies for projects
pip install matplotlib pillow
```

For detailed setup instructions, see [`00_setup_and_environment/`](#00-setup--environment)

## 📁 Project Structure

### 00. 🛠️ Setup & Environment (`00_setup_and_environment/`)
Development environment setup and virtual environment management:
- **`virtual_environment.py`** - Basic virtual environment demonstration with step-by-step comments
- **`README.md`** - Comprehensive guide for Python environment setup, best practices, and troubleshooting

### 01. 🎯 Fundamentals (`01_fundamentals/`)
Core Python concepts and building blocks:

#### Variables & Data Types (`01_variables_and_data_types/`)
- **`variables_and_data_types.py`** - Variable declaration, basic data types, type conversion

#### Functions & Scope (`02_functions_and_scope/`)
- **`functions_and_documentation.py`** - Function definition, parameters, return values, docstrings

### 02. 🔄 Control Structures (`02_control_structures/`)
Program flow control and decision making:

#### Conditionals (`01_conditionals/`)
- **`conditional_statements.py`** - If/elif/else statements, comparison operators, logical operators

#### Loops (`02_loops/`)
- **`loops_introduction.py`** - For loops, range function, nested loops
- **`while_loops.py`** - While loop implementation and use cases
- **`number_manipulation_loops.py`** - Number processing with loops
- **`even_number_operations.py`** - Even number filtering and operations

### 03. 📊 Data Structures (`03_data_structures/`)
Working with Python's built-in data structures:

#### Lists & Tuples (`01_lists_and_tuples/`)
- **`list_operations.py`** - List creation, manipulation, methods
- **`tuple_operations.py`** - Tuple usage, immutability, applications

#### Dictionaries (`02_dictionaries/`)
- **`dictionary_operations.py`** - Dictionary creation, key-value operations, methods

### 04. 📁 File Operations (`04_file_operations/`)
File handling and data persistence:

#### Text Files (`01_text_files/`)
- **`reading_text_files.py`** - Reading text files, file handling patterns
- **`writing_text_files.py`** - Writing to text files, file modes
- **`sample_data.txt`** - Sample text data for practice
- **`main_example.txt`** - Example text file
- **`command_output.txt`** - Command output sample

#### JSON Operations (`02_json_operations/`)
- **`json_read_write_operations.py`** - JSON serialization and deserialization
- **`country_travel_json.py`** - Practical JSON data manipulation
- **`countries_data.json`** - Sample country dataset
- **`names_data.json`** - Sample names dataset

### 05. ⚠️ Error Handling (`05_error_handling/`)
Exception management and error prevention:
- **`basic_exception_handling.py`** - Try-catch blocks, common exceptions
- **`custom_exceptions.py`** - Creating and using custom exception classes

### 06. 🏗️ Object-Oriented Programming (`06_object_oriented_programming/`)
Classes, objects, and OOP principles:
- **`book_class_example.py`** - Class definition, inheritance, polymorphism with Book/Ebook example

### 07. 📦 Modules & Packages (`07_modules_and_packages/`)
Code organization and reusability:
- **`arithmetic_module.py`** - Basic arithmetic operations module
- **`module_import_examples.py`** - Various import techniques and module usage patterns

### 08. 🎮 Interactive Applications (`08_interactive_applications/`)
User interaction and dynamic programs:
- **`quiz_game.py`** - Interactive quiz with scoring system
- **`travel_planner.py`** - Dream destination itinerary builder
- **`user_input_examples.py`** - Input validation and processing

### 09. 🚀 Projects (`09_projects/`)
Real-world applications and tools:

#### File Organizer (`file_organizer/`)
- **`automated_file_organizer.py`** - Utility for organizing files by extension into folders

#### Image Watermark Tool (`image_watermark_tool/`)
- **`watermark_images.py`** - Batch image watermarking application using PIL/Pillow
- **`input_images/`** - Directory for original images to be watermarked
- **`watermarked_images/`** - Output directory for processed images
- **`super_nought.ttf`** - Custom font file for watermark text
- **`requirements.txt`** - Project dependencies (Pillow)
- **`README.md`** - Comprehensive usage and installation guide

#### Weather Data Visualization (`weather_data_visualization/`)
- **`weather_visualization.py`** - CSV weather data analysis and matplotlib visualization
- **`data/weather.csv`** - Sample weather dataset for analysis
- **`requirements.txt`** - Project dependencies (matplotlib)
- **`README.md`** - Data format guide and customization instructions

### 10. 🛠️ Utilities & Libraries (`10_utilities_and_libraries/`)
Working with Python's standard library:
- **`datetime_operations.py`** - Date and time manipulation
- **`random_selections.py`** - Random number generation and selection
- **`mathematical_operations.py`** - Mathematical utilities and calculations

## 🎯 Learning Objectives

This workspace covers:

- **Development Environment**: Virtual environment setup, dependency management
- **Python Fundamentals**: Variables, data types, operators
- **Control Structures**: Conditionals, loops, iteration
- **Functions**: Definition, parameters, return values, documentation
- **Data Structures**: Lists, tuples, dictionaries
- **Object-Oriented Programming**: Classes, inheritance, polymorphism
- **File I/O**: Reading/writing text and JSON files
- **Error Handling**: Try-catch blocks, custom exceptions
- **Module System**: Imports, creating reusable modules
- **Interactive Programming**: User input, game development
- **Data Visualization**: Matplotlib plotting, CSV data analysis
- **Image Processing**: PIL/Pillow for image manipulation and watermarking
- **Practical Applications**: File organization, data processing, real-world tools

## 🛠️ Getting Started

### Prerequisites
- Python 3.7 or higher installed on your system
- Basic text editor or IDE (VS Code, PyCharm, etc.)

### Setup Instructions

1. **Environment Setup** (Recommended first step):
   ```bash
   # Create virtual environment
   py -m venv python_learning_env
   
   # Activate virtual environment
   python_learning_env\Scripts\activate  # Windows
   # source python_learning_env/bin/activate  # Linux/Mac
   ```

2. **Install Project Dependencies**:
   ```bash
   # For all projects
   pip install matplotlib pillow
   
   # Or install per project
   cd 09_projects/image_watermark_tool && pip install -r requirements.txt
   cd 09_projects/weather_data_visualization && pip install -r requirements.txt
   ```

### Running the Examples

1. **Environment & Setup**:
   ```bash
   python 00_setup_and_environment/virtual_environment.py
   ```

2. **Fundamentals Practice**:
   ```bash
   python 01_fundamentals/01_variables_and_data_types/variables_and_data_types.py
   python 01_fundamentals/02_functions_and_scope/functions_and_documentation.py
   ```

3. **Interactive Applications**:
   ```bash
   python 08_interactive_applications/quiz_game.py
   python 08_interactive_applications/travel_planner.py
   ```

4. **Real-World Projects**:
   ```bash
   # File organization
   python 09_projects/file_organizer/automated_file_organizer.py
   
   # Image watermarking (requires Pillow)
   python 09_projects/image_watermark_tool/watermark_images.py
   
   # Weather data visualization (requires matplotlib)
   python 09_projects/weather_data_visualization/weather_visualization.py
   ```

5. **Module System**:
   ```bash
   python 07_modules_and_packages/arithmetic_module.py
   python 07_modules_and_packages/module_import_examples.py
   ```

## 📖 Key Features

### Object-Oriented Programming Example
The `06_object_oriented_programming/book_class_example.py` demonstrates:
- Class definition and initialization
- Method implementation
- Inheritance with `Ebook` class extending `Book`
- Method overriding and `super()` usage
- String representation with `__str__`

### File Operations
Multiple examples of:
- Reading and writing text files
- JSON data handling
- Path operations using `pathlib`
- Error handling for file operations

### Interactive Applications
- Quiz game with scoring system
- Travel itinerary planner with user input
- Dynamic data collection and display

### Real-World Projects
- **Image Watermark Tool**: Batch image processing with PIL/Pillow for adding text watermarks
- **Weather Data Visualization**: CSV data analysis and matplotlib plotting for temperature trends
- **File Organizer**: Automatically sorts files by extension into organized folders
- **Arithmetic Module**: Reusable mathematical operations and calculations
- **Random Data Generators**: Utilities for generating and processing random data

## 🎮 Interactive Examples

### Quiz Game
Test your programming knowledge with an interactive quiz featuring:
- Multiple choice questions
- Score tracking
- Ability to quit anytime
- Immediate feedback

### Travel Planner
Plan your dream destinations with:
- Interactive destination input
- Optional notes for each location
- Beautiful output formatting
- Dynamic itinerary building

## 📝 Learning Path

1. **Environment Setup**: Start with `00_setup_and_environment/` - virtual environments and project setup
2. **Python Basics**: Begin with `01_fundamentals/` - variables, data types, and functions
3. **Control Flow**: Master `02_control_structures/` - conditionals and loops
4. **Data Structures**: Practice with `03_data_structures/` - lists, tuples, and dictionaries
5. **File Operations**: Learn I/O with `04_file_operations/` - text and JSON files
6. **Error Handling**: Understand `05_error_handling/` - exception management
7. **OOP Concepts**: Study `06_object_oriented_programming/` - classes and inheritance
8. **Modules**: Explore `07_modules_and_packages/` - code organization
9. **Interaction**: Build `08_interactive_applications/` - user-facing programs
10. **Real Projects**: Create `09_projects/` - image processing, data visualization, automation
11. **Standard Library**: Use `10_utilities_and_libraries/` - built-in Python features

## 🤝 Contributing

Feel free to add new examples, improve existing code, or suggest new learning exercises. This is a personal learning workspace that grows with your Python journey!

## 📚 Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 Style Guide](https://pep8.org/)

---

Happy Learning! 🐍✨