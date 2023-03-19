# python3  221RDB047


def parallel_processing(thread_count,job_count,times):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads=[]
    for index in range(thread_count):
        threads.append(0)
    time=0
    job_index=0
    
    while len(output)<job_count:
        for index in range(thread_count):
            if threads[index]<=time:
                output.append((index,time))
                threads[index]=time+times[job_index]
                job_index+=1
        time+=1
    
        

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    configuration= input().split()
    thread_count=int(configuration[0])
    job_count=int(configuration[1])

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    times = list(map(int,input().split()))

    # TODO: create the function
    result = parallel_processing(thread_count,job_count,times)
    
    # TODO: print out the results, each pair in it's own line
    for pair in result:
        print(pair[0],pair[1])



if __name__ == "__main__":
    main()
