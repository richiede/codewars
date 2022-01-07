def queue_time(customers, n):
    """
    There is a queue for the self-checkout tills at the supermarket.
    Your task is write a function to calculate the total time required
    for all the customers to check out.
    INPUT: customers: an array of positive integers representing the queue.
    Each integer represents a customer, and its value is
    the amount of time they require to check out.
    n: a positive integer, the number of checkout tills.
    OUTPUT: The function should return an integer, the total time required.
    CLARIFICATIONS
    There is only ONE queue serving many tills, and
    The order of the queue NEVER changes, and
    The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
    """
    till_queue = customers[0:n]
    count = 0
    del(customers[0:n])
    till_queue.sort()
    # main loop
    while len(till_queue) > 0:
        num = till_queue[0]
        count += num
        for i in range(len(till_queue)):
            till_queue[i] -= num
        till_queue = [x for x in till_queue if x != 0]
        num = n - len(till_queue)
        till_queue = till_queue + customers[0:num]
        till_queue.sort()
        del(customers[0:num])
    return count
        
    


print(queue_time([1,2,3,4,5], 100))
