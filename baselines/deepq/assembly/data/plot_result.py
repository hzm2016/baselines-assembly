# -*- coding: utf-8 -*-
"""
# @Time    : 24/10/18 2:40 PM
# @Author  : ZHIMIN HOU
# @FileName: plot_result.py
# @Software: PyCharm
# @Github    ： https://github.com/hzm2016
"""
import collections
import matplotlib.pyplot as plt
import numpy as np
import pickle
from baselines.deepq.assembly.src.value_functions import *

"""=================================Plot result====================================="""
YLABEL = ['Fx(N)', 'Fy(N)', 'Fz(N)', 'Mx(Nm)', 'My(Nm)', 'Mz(Nm)']
Title = ["X axis force", "Y axis force", "Z axis force",
         "X axis moment", "Y axis moment", "Z axis moment"]
High = np.array([40, 40, 0, 5, 5, 5, 542, -36, 188, 5, 5, 5])
Low = np.array([-40, -40, -40, -5, -5, -5, 538, -42, 192, -5, -5, -5])
"""================================================================================="""


def plot(result_path):
    plt.figure(figsize=(15, 15), dpi=100)
    plt.title('Search Result')
    prediction_result = np.load(result_path)
    for i in range(len(prediction_result)):
        for j in range(6):
            line = prediction_result[:, j]
            # plt.subplot(2, 3, j+1)
            plt.plot(line)
            plt.ylabel(YLABEL[j])
            plt.xlabel('steps')
            plt.legend(YLABEL)
    plt.show()


def plot_force_and_moment(path_2, path_3):
    V_force = np.load(path_2)
    V_state = np.load(path_3)
    plt.figure(figsize=(15, 10), dpi=100)
    plt.title("Search Result of Force", fontsize=20)
    plt.plot(V_force[:100])
    plt.xlabel("Steps", fontsize=20)
    plt.ylabel("F(N)", fontsize=20)
    plt.legend(labels=['Fx', 'Fy', 'Fz', 'Mx', 'My', 'Mz'], loc='best', fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    plt.figure(figsize=(15, 10), dpi=100)
    plt.title("Search Result of State", fontsize=20)
    plt.plot(V_state[:100] - [539.88427, -38.68679, 190.03184, 179.88444, 1.30539, 0.21414])
    plt.xlabel("Steps", fontsize=20)
    plt.ylabel("Coordinate", fontsize=20)
    plt.legend(labels=['x', 'y', 'z', 'rx', 'ry', 'rz'], loc='best', fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    plt.show()


def plot_reward(reward_path):
    reward = np.load(reward_path)
    print(reward[0])
    plt.figure(figsize=(15, 15), dpi=100)
    plt.title('Episode Reward')
    plt.plot(np.arange(len(reward) - 1), np.array(reward[1:]))
    plt.ylabel('Episode Reward')
    plt.xlabel('Episodes')
    plt.show()


def plot_raw_data(path_1):
    data = np.load(path_1)
    force_m = np.zeros((len(data), 12))

    plt.figure(figsize=(20, 20), dpi=100)
    plt.tight_layout(pad=3, w_pad=0.5, h_pad=1.0)
    plt.subplots_adjust(left=0.065, bottom=0.1, right=0.995, top=0.9, wspace=0.2, hspace=0.2)
    plt.title("True Data")
    for j in range(len(data)):
        force_m[j] = data[j, 0]
    k = -1
    for i in range(len(data)):
        if data[i, 1] == 0:
            print("===========================================")
            line = force_m[k+1:i+1]
            print(line)
            k = i
            for j in range(6):
                plt.subplot(2, 3, j + 1)
                plt.plot(line[:, j])
                # plt.plot(line[:, 0])

                if j == 1:
                    plt.ylabel(YLABEL[j], fontsize=17.5)
                    plt.xlabel('steps', fontsize=20)
                    plt.xticks(fontsize=15)
                    plt.yticks(fontsize=15)
                else:
                    plt.ylabel(YLABEL[j], fontsize=20)
                    plt.xlabel('steps', fontsize=20)
                    plt.xticks(fontsize=15)
                    plt.yticks(fontsize=15)
        i += 1
   # plt.savefig('raw_data_random_policy1.jpg')


def plot_continuous_data(path):
    raw_data = np.load(path)
    plt.figure(figsize=(20, 15), dpi=100)
    plt.title('Episode Reward')
    plt.tight_layout(pad=3, w_pad=0.5, h_pad=1.0)
    plt.subplots_adjust(left=0.065, bottom=0.1, right=0.995, top=0.9, wspace=0.2, hspace=0.2)
    plt.title("True Data")
    data = np.zeros((len(raw_data), 12))
    for j in range(len(raw_data)):
        data[j] = raw_data[j, 0]
    print(data[:, 0])
    for j in range(6):
        plt.subplot(2, 3, j + 1)
        plt.plot(data[:, j])
        plt.ylabel(YLABEL[j], fontsize=15)
        plt.xlabel('steps', fontsize=15)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
    plt.savefig('raw_data.jpg')
    plt.show()


# Plot the true prediction and true value
def plot_true_data():
    f = open('../data/learning_result_policy', 'rb')
    plot_value_functions = ['Move down Fy', 'Move down Fx', 'Move down Fz', 'Move down Mx', 'Move down My', 'Move down Mz']
    # plot_value_functions = ['Move down step']
    raw_data = pickle.load(f)
    plt.figure(figsize=(20, 15), dpi=100)
    plt.title('Episode Reward')
    plt.tight_layout(pad=3, w_pad=0.5, h_pad=1.0)
    plt.subplots_adjust(left=0.065, bottom=0.1, right=0.995, top=0.9, wspace=0.2, hspace=0.2)
    plt.title("True Data")
    # legend = sorted([key for key in plot_value_functions.keys()])
    # print(legend)
    # print(value_functions.keys())
    for j, key in enumerate(plot_value_functions):
        plt.subplot(2, 3, j + 1)
        plt.plot(raw_data[('GTD(1)', 'Hindsight Error')][key])
        plt.plot(raw_data[('GTD(1)', 'Prediction')][key])
        # plt.legend('True value', 'Prediction value')
        plt.ylabel(key, fontsize=15)
        plt.xlabel('steps', fontsize=15)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
    plt.show()


if __name__ == "__main__":
    # force = np.load('./search_force.npy')
    # state = np.load('./search_state.npy')
    # print(np.max(force, axis=0))
    # print(np.min(force, axis=0))
    # print(np.max(state, axis=0))
    # print(np.min(state, axis=0))
    # plot('./search_state.npy')
    # plot('./search_force.npy')
    # plot_reward('./episode_rewards.npy')

    # data = np.load('prediction_result.npy')
    # print(data[:, 2])
    # plot_continuous_data('prediction_result_1.npy')

    # f = open('../data/learning_result', 'rb')
    # y = pickle.load(f)
    # data = y[('GTD(1)', 'Hindsight Error')]['Move down Fz']
    # print(data)
    # plt.figure(figsize=(15, 15), dpi=100)
    # plt.title('Search Result')
    #
    # plt.plot(data)
    # plt.ylabel(YLABEL[0])
    # plt.xlabel('steps')
    # plt.legend(YLABEL)
    # plt.show()

    plot_true_data()

    # past_cumulants = collections.deque([0], maxlen=11)
    # past_cumulants.append(10)
    # past_cumulants.append(10)
    # past_cumulants.clear()
    # past_cumulants.append(10)
    # print(past_cumulants)