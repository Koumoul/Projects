import gym
import universe
import random

def determine_turn(turn, observation_n, j, total_sum, prev_total_sum, reward_n):
    #for every 15 iteration sum the total obersvationn and take the average
    #if lower than 0 change the direaction
    #if we go
    if(j >= 15):
        if(total_sum/ j ) == 0:
            turn= True
        else:
            turn = False
        #reset vars

        j = 0
        prev_total_sum = total_sum
        total_sum = 0
    else:
        turn = False
    if(observation_n != None):
        #increment counter and reward sum
        j+=1
        total_sum = total_sum + reward_n[0]
    return(turn, j, total_sum, prev_total_sum, )


def main():
    #init env
    env = gym.make('flashgames.CoasterRacer-v0')
    observation_n = env.reset()

    #init variable
    #num of game iteration
    n = 0
    j = 0
    #sum obersvation
    total_sum = 0
    prev_total_sum = 0
    turn = False

    #define our turn / jey board action

    left = [('KeyEvent', 'ArrowUp', True ),('KeyEvent', 'ArrowLeft', True ),('KeyEvent', 'ArrowRight', False ) ]
    right = [('KeyEvent', 'ArrowUp', True ),('KeyEvent', 'ArrowLeft', False ),('KeyEvent', 'ArrowRight', True ) ]
    forward = [('KeyEvent', 'ArrowUp', True ),('KeyEvent', 'ArrowLeft', False ),('KeyEvent', 'ArrowRight', False ) ]

    #main logic
    while True :
        #incremet a counter for number of iteration
        n+=1
        #if at least one iteration : check if turn is needed
        if(n>1):
            if(observation_n[0] != None):
                #store the reward in the previous score
                prev_score = reward_n[0]
            if(turn):
                #pick a random event
                #where to turn
                event = random.choice([left,right])
                #perform a action
                action_n = [event for ob in observation_n]
                #set turn to False
                turn = False
        elif(~turn):
            #if no turn is needed, go straight
            action_n = [forward for ob in observation_n]
        # if ther is a obersvation, game has started, check if turn needed
        if observation_n[0] != None :
            turn, j, total_sum, prev_total_sum = determine_turn(turn, observation_n[0], j, total_sum, prev_total_sum, reward_n)
        #save new variable for each oteration
        observation_n, reward_n, done_n, info = env.step(action_n)

        env.render()
if __name__ == '__main__':
    main()
