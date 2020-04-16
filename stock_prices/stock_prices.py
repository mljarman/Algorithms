#!/usr/bin/python

import argparse
prices = [1050, 3800, 270, 1540, 2]
def find_max_profit(prices):
    # set current min to first value, can only sell after buy:
    current_min = 0
    # set current max profit to difference between first and second values
    current_max_profit = prices[1] - prices[0]
    # loop through list, buy price can't be last in the list:
    for i in range(len(prices)-1):
        # store current minimum price:
        if prices[i] < prices[current_min]:
            current_min = i
            print(f'min: {prices[current_min]}')
            # loop through numbers after current_min and calculate profit:
            for x in range(current_min + 1, len(prices)):
                profit = prices[x] - prices[current_min]
                # store largest max_profit:
                if profit > current_max_profit:
                    current_max_profit = profit
                    print(f'cur_profit: {current_max_profit}')
    return current_max_profit

find_max_profit(prices)
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
