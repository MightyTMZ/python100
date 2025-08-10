def check_braces(text):
    stack = []
    closeToOpen = { ")" : "(", "]": "[", "}": "{"}

    for c in text:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
        
    return True if not stack else False
