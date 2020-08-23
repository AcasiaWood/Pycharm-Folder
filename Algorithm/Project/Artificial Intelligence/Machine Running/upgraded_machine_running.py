# matrix module
import numpy

# it is created to solve scientific analysis algorithm modules, numerical integration, differential equations, etc.
# but only the sigmoid function is used here.
import scipy.special

import gzip

# neural network class definition
class NeuralNetwork:
    # neural network initialization
    def __init__(self, input_node, hidden_node, output_node, learning_rate):
        self.input_node = input_node
        self.hidden_node = hidden_node
        self.output_node = output_node
        self.learning_rate = learning_rate

        # weight matrix weight of input -> hidden
        # weight matrix weight of hidden -> output
        # set the median value to 0.0, standard deviation rooted in the number of nodes, and inverse
        # extract random values ​​from the probability distribution plot created above

        self.wih = numpy.random.normal(0.0, pow(self.hidden_node, -0.5), (self.hidden_node, self.input_node))
        self.who = numpy.random.normal(0.0, pow(self.output_node, -0.5), (self.output_node, self.hidden_node))

        # use the sigmoid function as the activation function
        self.activation_function = lambda x: scipy.special.expit(x)

    # neural network learning
    def train(self, input_list, target_list):
        # convert the input list to a two-dimensional chariot matrix
        inputs = numpy.array(input_list, ndmin=2).T

        # convert the output list to a two-dimensional vehicle matrix
        targets = numpy.array(target_list, ndmin=2).T

        # calculate the signal back to the hidden layer
        hidden_input = numpy.dot(self.wih, inputs)

        # calculate the signal from the hidden layer to the output layer
        hidden_output = self.activation_function(hidden_input)

        # compute the signal back to the output layer
        target_input = numpy.dot(self.who, hidden_output)

        # calculate the signal from the output layer
        target_output = self.activation_function(target_input)

        # above, the signal is passed in order of "input node -> hidden node -> output node"

        # calculate the error between the output layer and the actual value (error = actual value-result value)
        target_error = targets - target_output

        # calculate the error of the hidden layer (manufacture the error of the output layer divided by weight)
        hidden_error = numpy.dot(self.who.T, target_error)

        # weight update between hidden layer and output layer (reverse propagation occurs)
        self.who += self.learning_rate * numpy.dot((target_error * target_output * (1.0 - target_output)),
                                                   numpy.transpose(hidden_output))
        self.wih += self.learning_rate * numpy.dot((hidden_error * hidden_output * (1.0 - hidden_output)),
                                                   numpy.transpose(inputs))

    # neural network query
    def query(self, input_list):
        # convert input list to two-dimensional electronic matrix
        inputs = numpy.array(input_list, ndmin=2).T

        # calculate the signal back to the hidden layer
        hidden_input = numpy.dot(self.wih, inputs)

        # calculate the signal from the hidden layer to the output layer
        hidden_output = self.activation_function(hidden_input)

        # compute the signal back to the output layer
        target_input = numpy.dot(self.who, hidden_output)

        # calculate the outgoing signal from the output layer
        target_output = self.activation_function(target_input)

        return target_output

# number of input, hidden, and output nodes
input_node = 784
hidden_node = 200
output_node = 10

# learning rate
learning_rate = 0.1

# neural network object creation
number = NeuralNetwork(input_node, hidden_node, output_node, learning_rate)


# Neural network learning

# Open the "train mnist" file
# "train mnist" files are not supported. Please contact us by email to download the file.
with gzip.open("mnist_train.gz", 'r') as f:
    train_data_list = [x.decode('utf8').strip() for x in f.readlines()]
    f.close()

# additional learning settings
epoch = 1
train_cnt = 0

for i in range(epoch):
    for record in train_data_list:
        # separated by commas
        all_value = record.split(',')

        # adjusting the range and value of input
        inputs = (numpy.asfarray(all_value[1:]) / 255.0 * 0.99) + 0.01

        # generate result value (actual value is 0.99, the rest is 0.01)
        target = numpy.zeros(output_node) + 0.01

        # all_value[0] is the result value for this record
        target[int(all_value[0])] = 0.99

        number.train(inputs, target)

        train_cnt += 1

        if train_cnt % 100 == 0:
            print("epoch", i+1, "train count: ", train_cnt)

    train_cnt = 0

# Neural network test
# Open the experimental file
with gzip.open("mnist_test.gz", 'r') as f:
    test_data_list = [x.decode('utf8').strip() for x in f.readlines()]
    f.close()

# initialize the report card, which is a performance indicator of the neural network, to have no value
scorecard = []

for record in test_data_list:
    # separate results with commas
    all_value = record.split(',')

    # the correct answer is the first value
    correct_label = int(all_value[0])

    # initialize range value of input value
    inputs = (numpy.asfarray(all_value[1:]) / 255.0 * 0.99) + 0.01

    # query the neural network
    outputs = number.query(inputs)
    print("data target entered: ", correct_label)
    print("target derived from neural network: ", numpy.argmax(outputs))
    print("========================================")

    # the index of the highest value matches the index of the label
    label = numpy.argmax(outputs)

    # add correct or incorrect answers to the list
    if label == correct_label:
        # if correct, add 1 to the report card
        scorecard.append(1)
    else:
        scorecard.append(0)

# calculate and print out the correct answer rate
scorecard_array = numpy.asarray(scorecard)
print("grade =", scorecard_array.sum() / scorecard_array.size, ',', "total:", scorecard_array.size)
print("========================================")
