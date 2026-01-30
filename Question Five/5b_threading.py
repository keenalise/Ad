import threading

# Global arrays as suggested by the brief [cite: 266, 268]
original_list = [7, 12, 19, 3, 18, 4, 2, 6, 15, 8]
sorted_list = [0] * len(original_list)

def sorting_thread_func(start_index, end_index):
    """Sorts a specific portion of the global array[cite: 271, 272]."""
    # Using built-in sort for the sublist
    sublist = original_list[start_index:end_index]
    sublist.sort()
    # Placing sorted sublist back into the original list's segment
    original_list[start_index:end_index] = sublist
    print(f"Thread sorting range {start_index} to {end_index}: {sublist}")

def merging_thread_func(mid):
    """Merges two sorted halves into the second global array[cite: 265, 269]."""
    left_half = original_list[:mid]
    right_half = original_list[mid:]
    
    i = j = k = 0
    # Classic merge logic
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_list[k] = left_half[i]
            i += 1
        else:
            sorted_list[k] = right_half[j]
            j += 1
        k += 1
        
    # Append remaining elements
    while i < len(left_half):
        sorted_list[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        sorted_list[k] = right_half[j]
        j += 1
        k += 1
    print(f"Merging thread completed. Result: {sorted_list}")

def main():
    print(f"Original List: {original_list}")
    mid = len(original_list) // 2
    
    # Create the two sorting threads 
    t0 = threading.Thread(target=sorting_thread_func, args=(0, mid))
    t1 = threading.Thread(target=sorting_thread_func, args=(mid, len(original_list)))
    
    # Start sorting threads
    t0.start()
    t1.start()
    
    # Wait for sorting threads to finish before merging
    t0.join()
    t1.join()
    
    # Create and start the merging thread
    t_merge = threading.Thread(target=merging_thread_func, args=(mid,))
    t_merge.start()
    t_merge.join()
    
    # Final output from parent thread 
    print(f"Final Sorted List: {sorted_list}")

if __name__ == "__main__":
    main()