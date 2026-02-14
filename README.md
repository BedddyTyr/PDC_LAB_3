# PDC_LAB_3
Marabe\
Misajon\
Orencia\
Samuya\
Sonquipal


## Analysis Questions
1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division.
- Task parallelism executes different computations simultaneously on the same input, while data parallelism executes the same   computation across multiple inputs. In the lab activity, Part A shows parallelism because multiple deductions functions run concurrently for one employee, dividing the work by function. Part B shows parallelism because a single payroll function runs concurrently for MULTIPLE employees, this divides work by records.

2. Explain how concurrent.futures managed execution, including submit(), map(), and Future objects. Discuss the purpose of with when creating an Executor.
- the module manages concurrency through executors that schedule tasks on workers. Part A uses submit() to send individual deduction functions to the pool and returns future objects which is used by .result(). Part B uses map() to do the same. The "with" statement ensures proper startup and automatic shutdown of workers, preventing resource leaks.

3. Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did true parallelism occur?
- ThreadPoolExecutor does not provide true parallelism because of Python's Global Interpreter Lock (GIL), which allows only one thread to execute bytecode at a time. 

4. Explain why ProcessPoolExecutor enables true parallelism, including memory space separation and GIL behavior.
- ProcessPoolExecutor enables true parallelism because each worker runs in a separate process with its own interpreter, memory space, and GIL.

5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why?
- the process-based approach scales much better because it distributes records across cores and maintains REAL parallel execution.

6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use.
- In a real payroll system, task parallelism would be used when processing one employee, allowing deductions, overtime, bonuses, and taxes to run concurrently, where ThreadPoolExecutor is appropriate. While ProcessPoolExecutor will perform better when processing payroll for MANY employees at ones, where the same payroll function run accross records.
