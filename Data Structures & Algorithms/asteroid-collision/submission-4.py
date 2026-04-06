class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # Handle collisions
            while stack and a < 0 < stack[-1]:
                if abs(a) > abs(stack[-1]):
                    # Incoming asteroid is larger, destroy the top of stack
                    stack.pop()
                    # Continue checking against the next asteroid in stack
                elif abs(a) == abs(stack[-1]):
                    # Both asteroids destroy each other
                    stack.pop()
                    a = 0
                    break
                else:
                    # Top of stack is larger, incoming asteroid is destroyed
                    a = 0
                    break
            
            # If the asteroid wasn't destroyed, add it to the stack
            if a != 0:
                stack.append(a)
        
        return stack