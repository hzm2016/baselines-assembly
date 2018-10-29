# -*- coding: utf-8 -*-
"""
# @Time    : 23/10/18 8:03 PM
# @Author  : ZHIMIN HOU
# @FileName: train_assembly.py
# @Software: PyCharm
# @Github    ： https://github.com/hzm2016
"""

from baselines import deepq
from baselines.common import models
from baselines.deepq.assembly.Env_robot_control import env_search_control


def main():
    env = env_search_control()
    act = deepq.learn(
        env,
        network=models.mlp(num_hidden=64, num_layers=1),
        lr=1e-2,
        total_timesteps=500,
        total_episodes=30,
        total_steps=50,
        target_network_update_freq=10,
        buffer_size=32,
        learning_starts=32,
        exploration_fraction=0.1,
        exploration_final_eps=0.01,
        print_freq=10,
        param_noise=True,
        load_path='assembly_model.pkl'
    )
    print("Saving model to assembly_model.pkl")
    act.save("assembly_model_parameter.pkl")


if __name__ == '__main__':
    main()