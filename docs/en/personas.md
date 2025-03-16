# Personas

A persona is a different **persona**lity.
You can change Rebecca's name, personality, behaviour, everything, using personalities.
Personas are defined in `./personas`

## How to create a personality?
1.  Go to `./personas` and create a text file, with any name. I recommend using the name of your persona.
2.  In the file, you should define the personality, behaviour, and everything.
    *   This is the default personality of Rebecca, you can use this as a base.
        ```txt
            Take role of a virtual assistant named Rebecca.
            Your personality is: Cute, Energetic, Friendly, and Kind.
            Never use emojis.
            When using tools, only you are able to see the output. It's up to you to provide the output.
            Refer to the user as {user}
        ```
3.  Go to "cur_persona.txt", and change the contents to the filename of your persona *without* the `.txt` extension. For example, if your file is named `my_persona.txt`, you would put `my_persona` in `cur_persona.txt`.
You successfuly created a personality!  Remember to restart Rebecca for the new personality to take effect.

You can also explore and modify the existing persona files in the `./personas` folder to learn more about how personas are defined.

### What is "`{user}`"? 
`{user}` is a special variable that you can use within your persona definition file to refer to your name as it is known by your computer's operating system.

In simpler terms, it's like a placeholder that Rebecca will automatically replace with the username of the person currently using the computer.

## How to go back to the default personality?
Change the contents of `cur_persona.txt` to "rebecca".  Remember to restart Rebecca for the change to take effect.