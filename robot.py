import random
import brain

#下棋的机器人类
class Crobot():
    def __init__(self,flag,mode):  #flag指定机器人执蓝为1，执红色为-1；mode指定运行模式：0为随机模式brain_random，
        self.flag=flag
        self.mode=mode
        if mode==1:
            self.brain_dqn_train=brain.Cbrain()

    def move(self,s,movemode=-1):  #movemode用于指定这一步的模式：默认-1为跟随生成机器人时的指定，0为随机下法，1为DQN训练模式，2为DQN专家模式
        if movemode==-1:
            movemode=self.mode

        #随机模式
        if movemode==0:
            x,y= self.brain_random(s)
            return x,y,self.flag

        #DQN训练模式
        if movemode==1:
            #选动作
            a=self.brain_dqn_train.choose_action(s)
            x,y =divmod(a,3)  #divmod(x,y)这个函数可以获得商和余数，比如divmod(5,2)，返回的值为(2,1)，其中2为商，1为余数
            return x,y,self.flag

        #DQN专家模式（提取已经训练好的神经网络）
        #if movemode==2:

    def brain_random(self, s):  # 随机模式
        while 1:
            x = random.randrange(0, 3)
            y = random.randrange(0, 3)
            if s[x*3+y] == 0.:
                return x, y


    # def brain_random(self,m):  #随机模式
    #     while 1:
    #         x = random.randrange(0, 3)
    #         y = random.randrange(0, 3)
    #         if m[x][y] == 0:
    #             return x, y

    # def brain_dqn_train(self,m):  #DQN训练模式
    #     m1d=[0]*9  #把m转为1维，存入m1d方便使用，不过貌似tf.layers.dense函数会自动压扁输入的值，空了试试
    #     k=0
    #     for i in range(3):
    #         for j in range(3):
    #             m1d[k]=m[i][j]
    #             k+=1
    #
    #     # tf计算图
    #     tf_s = tf.placeholder(tf.int32, [None, self.N_STATES])
    #     tf_a = tf.placeholder(tf.int32, [None, ])
    #     tf_r = tf.placeholder(tf.float32, [None, ])
    #     tf_s_ = tf.placeholder(tf.int32, [None, self.N_STATES])
    #
    #     with tf.variable_scope('q'):  # evaluation network，q就是q值，即q[0]...q[N_ACTIONS]，就是各动作的q值
    #         l_eval = tf.layers.dense(tf_s, self.UNITNUM, tf.nn.relu, kernel_initializer=tf.random_normal_initializer(0, 0.1))
    #         q = tf.layers.dense(l_eval, self.N_ACTIONS, kernel_initializer=tf.random_normal_initializer(0, 0.1))  #q估计值，这个q估计典型的可以是q[0]=0.8,q[1]=0.9,q[2]=0.2等等
    #
    #     with tf.variable_scope('q_next'):  # target network, not to train
    #         l_target = tf.layers.dense(tf_s_, self.UNITNUM, tf.nn.relu, trainable=False)
    #         q_next = tf.layers.dense(l_target, self.N_ACTIONS, trainable=False)
    #
    #     q_target = tf_r + self.GAMMA * tf.reduce_max(q_next, axis=1)  # shape=(None, ),  #q现实值
    #
    #     #下面两步是把
    #     a_one_hot = tf.one_hot(tf_a, depth=self.N_ACTIONS, dtype=tf.float32)
    #     q_wrt_a = tf.reduce_sum(q * a_one_hot, axis=1)  # shape=(None, ), q for current state
    #
    #     loss = tf.reduce_mean(tf.squared_difference(q_target, q_wrt_a))
    #     train_op = tf.train.AdamOptimizer(self.LR).minimize(loss)
    #
    #     #启动会话
    #     sess = tf.Session()
    #     sess.run(tf.global_variables_initializer())
    #
    #     def choose_action(s):
    #         #s = s[np.newaxis, :]------------------------------------------------------------
    #         if np.random.uniform() < self.EPSILON:
    #             # forward feed the observation and get q value for every actions
    #             actions_value = sess.run(q, feed_dict={tf_s: s})
    #             action = np.argmax(actions_value)
    #         else:
    #             action = np.random.randint(0, self.N_ACTIONS)
    #         return action
    #
    #     def store_transition(s, a, r, s_):
    #         #global MEMORY_COUNTER
    #         transition = np.hstack((s, [a, r], s_))
    #         # replace the old memory with new memory
    #         index = self.MEMORY_COUNTER % self.MEMORY_CAPACITY
    #         self.MEMORY[index, :] = transition
    #         self.MEMORY_COUNTER += 1
    #
    #     def learn():
    #         # update target net
    #         global LEARNING_STEP_COUNTER
    #         if LEARNING_STEP_COUNTER % self.TARGET_REPLACE_ITER == 0:
    #             t_params = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope='q_next')
    #             e_params = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope='q')
    #             sess.run([tf.assign(t, e) for t, e in zip(t_params, e_params)])
    #         LEARNING_STEP_COUNTER += 1
    #
    #         # learning
    #         sample_index = np.random.choice(self.MEMORY_CAPACITY, self.BATCH_SIZE)
    #         b_memory = self.MEMORY[sample_index, :]
    #         b_s = b_memory[:, :self.N_STATES].astype(int)
    #         b_a = b_memory[:, self.N_STATES].astype(int)
    #         b_r = b_memory[:, self.N_STATES + 1]
    #         b_s_ = b_memory[:, -self.N_STATES:].astype(int)
    #         sess.run(train_op, {tf_s: b_s, tf_a: b_a, tf_r: b_r, tf_s_: b_s_})
    #
    #     # print('\nCollecting experience...')
    #     # for i_episode in range(400):
    #     #     s = env.reset()
    #     #     ep_r = 0
    #     #     while True:
    #     #         env.render()
    #     #         a = choose_action(s)
    #     #
    #     #         # take action
    #     #         s_, r, done, info = env.step(a)
    #     #
    #     #         # modify the reward----------------------------------------------------------------------------
    #     #         # x, x_dot, theta, theta_dot = s_
    #     #         # r1 = (env.x_threshold - abs(x)) / env.x_threshold - 0.8
    #     #         # r2 = (env.theta_threshold_radians - abs(theta)) / env.theta_threshold_radians - 0.5
    #     #         # r = r1 + r2
    #     #
    #     #         store_transition(s, a, r, s_)
    #     #
    #     #         ep_r += r
    #     #         if MEMORY_COUNTER > MEMORY_CAPACITY:
    #     #             learn()
    #     #             if done:
    #     #                 print('Ep: ', i_episode,
    #     #                       '| Ep_r: ', round(ep_r, 2))
    #     #
    #     #         if done:
    #     #             break
    #     #         s = s_
    #
    #     return x,y





