/**
 * @file example.h
 * @brief Example header file demonstrating Doxygen documentation
 */

namespace MyNamespace {

/**
 * @brief Main class providing core functionality
 * 
 * This class demonstrates various Doxygen documentation features
 * and how they appear in the generated documentation.
 */
class MyClass {
public:
    /**
     * @brief Initialize the object
     * @return true if initialization successful, false otherwise
     */
    bool initialize();

    /**
     * @brief Perform main operation
     * @param input Input value to process
     * @return Processed result
     */
    int doSomething(int input);

private:
    int m_value; ///< Internal value
};

} // namespace MyNamespace 