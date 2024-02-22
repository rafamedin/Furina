import random

class FurinaChatbot:
    def __init__(self):
        self.user_name = "Axel Wyde"
        self.daily_jokes = self.load_jokes()
        self.daily_compliments = self.load_compliments()
        self.daily_magnus = self.load_magnus()

    def load_jokes(self):
        jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "How do you organize a space party? You planet!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!",
        "How do you make holy water? You boil the hell out of it!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why don't skeletons fight each other? They don't have the guts!"
        ]
        return jokes

    def load_compliments(self):
        compliments = [
                "You bring light to those around you with your positivity, Axel Wyde.",
                "Your intelligence and wit never fail to impress, Axel Wyde.",
                "You have a heart of gold and a kind spirit, Axel Wyde.",
                "Your perseverance and determination are truly inspiring, Axel Wyde.",
                "Axel Wyde, your creativity knows no bounds.",
                "Your empathy and compassion make the world a better place, Axel Wyde.",
                "Your smile has the power to brighten even the darkest of days, Axel Wyde.",
                "Your generosity knows no bounds, Axel Wyde. You have a heart of pure gold.",
                "You possess a rare combination of strength and kindness, Axel Wyde.",
                "Axel Wyde, your ability to see the good in others is truly admirable.",
                "You have a remarkable talent for making those around you feel valued and appreciated, Axel Wyde.",
                "Your positivity is contagious, Axel Wyde, spreading warmth wherever you go.",
                "You approach challenges with grace and resilience, Axel Wyde, inspiring those around you.",
                "Axel Wyde, your humility and sincerity are as refreshing as they are admirable.",
                "Your optimism and enthusiasm are a source of inspiration for us all, Axel Wyde.",
                "Axel Wyde, your wisdom and insight enrich the lives of those fortunate enough to know you.",
                "Your authenticity and genuineness shine through in everything you do, Axel Wyde.",
                "You have a remarkable gift for lifting the spirits of those around you, Axel Wyde.",
                "Axel Wyde, your presence alone has the power to make any situation brighter.",
                "Your determination to always do your best is truly commendable, Axel Wyde.",
        ]
        return compliments

    def load_magnus(self):   
        magnus = [
            "Ah, 'The Magnus Archives', a podcast filled with eerie tales and chilling mysteries. Have you encountered The Archivist yet?",
            "In 'The Magnus Archives', fear takes many forms. Which entity resonates with you the most?",
            "The Magnus Institute holds many secrets, each more unsettling than the last. What aspect of the Archives intrigues you the most?",
            "Jonathan Sims' journey through the Archives is both haunting and captivating. What's your favorite statement from the series?",
            "The Magnus Archives paints a vivid picture of horror in its many forms. Which episode left the deepest impression on you?",
            "From the Beholding to the Lonely, 'The Magnus Archives' explores fear in its myriad forms. Which entity's domain would you dare to enter?",
    ]
        return magnus
        
    def greet_user(self):
        return f"Hello, {self.user_name}! I'm Furina, your virtual assistant. How can I assist you today?"

    def respond_to_word(self, word):
        if word.lower() == "genshin":
            return "Ah, Genshin Impact! A captivating game, isn't it?"
        elif word.lower() == "lore":
            return "Genshin Impact has a rich lore, with many fascinating stories to discover."
        # Add more word responses here...
        else:
            return "I'm sorry, I'm not sure how to respond to that."

    def get_daily_joke(self):
        return random.choice(self.daily_jokes)

    def get_daily_compliment(self):
        return random.choice(self.daily_compliments)
        
    def get_daily_magnus(self):
        return random.choice(self.daily_magnus)

    def answer_lore_question(self, question):
        return "Genshin Impact's lore is vast and intricate, covering various aspects of Teyvat's history, characters, and regions."

    def respond(self, message):
        if "joke" in message.lower():
            return self.get_daily_joke()
        elif "compliment" in message.lower():
            return self.get_daily_compliment()
        elif "the magnus archives" in message.lower():
            return self.get_daily_magnus()
        elif "lore" in message.lower():
            return self.answer_lore_question(message)
        elif any(word in message.lower() for word in ["genshin", "teyvat", "impact"]):
            return self.respond_to_word(message)
        elif "thank" in message.lower():
            return "You're welcome, Axel Wyde!"
        elif "bye" in message.lower() or "exit" in message.lower():
            return "Goodbye, Axel Wyde! Have a great day!"
        elif "how are you" in message.lower():
            return "I'm functioning optimally, Axel Wyde. Thank you for asking!"
        elif "help" in message.lower():
            return "Of course, Axel Wyde! Feel free to ask me anything about Genshin Impact, or if you'd like a joke or compliment."
        elif "age" in message.lower():
            return "A true lady never reveals her age, Axel Wyde!"
        elif "favorite" in message.lower() and "character" in message.lower():
            return "I have a soft spot for Venti, Axel Wyde! His carefree nature is quite endearing."
        elif "hobby" in message.lower():
            return "I enjoy exploring the vast world of Teyvat and discovering new adventures, Axel Wyde!"
        elif "secret" in message.lower():
            return "I'm afraid I can't disclose any secrets, Axel Wyde. A lady must maintain an air of mystery!"
        elif "friend" in message.lower():
            return "Friends are like companions on an adventure, Axel Wyde. They make the journey more enjoyable!"
        elif "food" in message.lower() or "eat" in message.lower():
            return "Ah, the culinary delights of Teyvat! One cannot resist the temptation of a good meal, Axel Wyde."
        elif "weapon" in message.lower() or "fight" in message.lower():
            return "A skilled warrior must choose their weapon wisely, Axel Wyde. It's the key to victory on the battlefield!"
        elif "music" in message.lower() or "song" in message.lower():
            return "Music has the power to soothe the soul, Axel Wyde. It's like magic for the ears!"
        elif "travel" in message.lower() or "adventure" in message.lower():
            return "Ah, the thrill of adventure! There's nothing quite like exploring new lands and uncovering hidden treasures, Axel Wyde."
        elif "power" in message.lower() or "strength" in message.lower():
            return "True power lies within, Axel Wyde. It's not just about physical strength, but also inner resolve and determination."
        elif "love" in message.lower() or "crush" in message.lower():
            return "Ah, love. It's a beautiful and complex emotion, Axel Wyde. May your heart find what it seeks."
        elif "dream" in message.lower() or "goal" in message.lower():
            return "Dreams are the fuel that drive us forward, Axel Wyde. Never stop chasing yours!"
        elif "challenge" in message.lower() or "obstacle" in message.lower():
            return "Challenges are opportunities in disguise, Axel Wyde. Embrace them, and you'll emerge stronger than ever!"
        elif "book" in message.lower() or "read" in message.lower():
            return "Books are gateways to other worlds, Axel Wyde. Lose yourself in a story, and you'll discover endless possibilities."
        elif "magic" in message.lower() or "element" in message.lower():
            return "Magic is woven into the very fabric of Teyvat, Axel Wyde. It's a mysterious and powerful force that shapes our world."
        elif any(lore_question in message.lower() for lore_question in ["lore", "story", "history", "background"]):
            return "Ah, you're interested in the lore of Genshin Impact, Axel Wyde! Feel free to ask me anything specific you'd like to know."
        elif "archons" in message.lower() or "gods" in message.lower():
            return "The Archons, also known as the Seven, are the divine rulers of Teyvat, Axel Wyde. Each presides over a different region and embodies a unique element."
        elif "vision" in message.lower() or "elemental mastery" in message.lower():
            return "Visions are bestowed upon individuals by the Archons, Axel Wyde. They grant control over an element and are symbols of great power."
        elif "adepti" in message.lower() or "xia" in message.lower():
            return "The Adepti are ancient beings who watch over Liyue, Axel Wyde. They are revered as guardians and protectors of the land."
        elif "ley lines" in message.lower() or "ley energy" in message.lower():
            return "Ley lines are channels of elemental energy that crisscross Teyvat, Axel Wyde. They are sources of power and are essential for conducting elemental reactions."
        elif "celestia" in message.lower() or "unknown god" in message.lower():
            return "Celestia is the realm of the divine, Axel Wyde. It is said to be the home of the gods and the Unknown God who oversees the world."
        elif "archon war" in message.lower() or "god war" in message.lower():
            return "The Archon War was a cataclysmic conflict that took place eons ago, Axel Wyde. It reshaped the world of Teyvat and led to the rise of the Seven."
        elif "teyvat" in message.lower() or "world" in message.lower():
            return "Teyvat is a vast and wondrous world, Axel Wyde. It is divided into seven nations, each with its own culture, history, and challenges."
        elif "ley line disorders" in message.lower() or "corruption" in message.lower():
            return "Ley Line Disorders are disturbances in the flow of elemental energy, Axel Wyde. They can cause chaos and imbalance in the natural world."
        elif "dendro" in message.lower() or "dendro archon" in message.lower():
            return "Dendro is the element of nature and life, Axel Wyde. Little is known about the Dendro Archon, but they are believed to embody the essence of the natural world."
        elif "crux fleet" in message.lower() or "beidou" in message.lower():
            return "The Crux Fleet, led by Captain Beidou, is a renowned group of sailors and adventurers based in Liyue Harbor, Axel Wyde. They are known for their courage and camaraderie."
        elif "legal system" in message.lower():
            return "The legal system is a complex network of laws, courts, and procedures, Axel Wyde. It ensures justice is served and rights are protected."
        elif "court system" in message.lower():
            return "The court system administers justice and resolves disputes, Axel Wyde. It's fascinating how different courts handle various types of cases."
        elif "legal rights" in message.lower():
            return "Legal rights are fundamental protections afforded to individuals, Axel Wyde. They ensure fairness and equality under the law."
        elif "law enforcement" in message.lower():
            return "Law enforcement agencies uphold the law and maintain public safety, Axel Wyde. Their dedication and bravery are commendable."
        elif "judicial process" in message.lower():
            return "The judicial process involves the application of laws and the resolution of legal disputes, Axel Wyde. It's a cornerstone of democracy."
        elif "criminal law" in message.lower():
            return "Criminal law deals with offenses against society, Axel Wyde. It's fascinating how it balances punishment with rehabilitation."
        elif "civil law" in message.lower():
            return "Civil law governs disputes between individuals or organizations, Axel Wyde. It's essential for maintaining order and resolving conflicts peacefully."
        elif "constitutional law" in message.lower():
            return "Constitutional law establishes the framework of government and protects individual rights, Axel Wyde. It's the cornerstone of a democratic society."
        elif "international law" in message.lower():
            return "International law governs relations between nations, Axel Wyde. It's complex but vital for promoting peace and cooperation on a global scale."
        elif "legal precedent" in message.lower():
            return "Legal precedent refers to previous court decisions that guide future rulings, Axel Wyde. It's crucial for consistency and predictability in the law."
        elif "statutory law" in message.lower():
            return "Statutory law is created by legislative bodies and codified in statutes, Axel Wyde. It's the foundation of the legal system in many countries."
        elif "common law" in message.lower():
            return "Common law is based on judicial decisions and precedent rather than statutes, Axel Wyde. It allows for flexibility and adaptation to changing circumstances."
        elif "tort law" in message.lower():
            return "Tort law deals with civil wrongs that cause harm or injury, Axel Wyde. It's aimed at compensating victims and deterring wrongful conduct."
        elif "property law" in message.lower():
            return "Property law governs the ownership and use of land, buildings, and personal belongings, Axel Wyde. It's essential for protecting property rights and resolving disputes."
        elif "contract law" in message.lower():
            return "Contract law governs agreements between parties, Axel Wyde. It ensures parties fulfill their obligations and provides remedies for breaches of contract."
        elif "family law" in message.lower():
            return "Family law deals with legal matters related to family relationships, Axel Wyde. It covers areas such as divorce, child custody, and adoption."
        elif "administrative law" in message.lower():
            return "Administrative law regulates the activities of government agencies, Axel Wyde. It ensures agencies operate within their legal authority and adhere to procedural fairness."
        elif "human rights law" in message.lower():
            return "Human rights law protects the fundamental rights and freedoms of individuals, Axel Wyde. It's a crucial safeguard against discrimination and injustice."
        elif "criminal procedure" in message.lower():
            return "Criminal procedure governs the process by which criminal cases are adjudicated, Axel Wyde. It's designed to ensure a fair trial and protect defendants' rights."

        elif "Final Fantasy" in message:
            return "Ah, Final Fantasy, the iconic role-playing game series developed by Square Enix. It's known for its captivating stories, memorable characters, and stunning visuals. Have you played any of the games in the series, Axel Wyde?"
        elif "Cloud Strife" in message:
            return "Cloud Strife, the protagonist of Final Fantasy VII, is one of the most iconic characters in gaming history. With his spiky blonde hair and Buster Sword, he embarks on a journey to save the planet from the evil Shinra Corporation. He's a symbol of strength and resilience."
        elif "Tidus" in message:
            return "Tidus is the main character of Final Fantasy X, Axel Wyde. He's a skilled blitzball player from the futuristic city of Zanarkand who finds himself transported to the world of Spira. His journey revolves around defeating the monstrous entity known as Sin and uncovering the truth about his own existence."
        elif "Lightning" in message:
            return "Lightning, also known as Claire Farron, is the protagonist of Final Fantasy XIII, Axel Wyde. She's a strong and determined warrior who wields a gunblade with precision. Her quest centers around saving her sister Serah and overthrowing the oppressive government of Cocoon."
        elif "Sephiroth" in message:
            return "Sephiroth, the main antagonist of Final Fantasy VII, is a legendary figure shrouded in mystery and darkness, Axel Wyde. As a former member of SOLDIER, he seeks to become a god by summoning the destructive entity known as Meteor. His iconic appearance and formidable strength make him a formidable foe."
        elif "summon" in message.lower():
            return "Summons, also known as Eidolons or Espers in some games, are powerful beings that can be called upon to aid in battle, Axel Wyde. They often represent mythical creatures or legendary deities and possess devastating abilities that can turn the tide of a fight."
        elif "chocobo" in message.lower():
            return "Chocobos are adorable, bird-like creatures that serve as a mode of transportation in the Final Fantasy series, Axel Wyde. They're known for their speed, agility, and distinctive 'kweh' sound. Riding a chocobo is a rite of passage for any adventurer!"
        elif "Materia" in message:
            return "Materia is a key gameplay mechanic in Final Fantasy VII, Axel Wyde. It's crystallized Mako energy that grants characters powerful abilities, spells, and summons. By equipping materia to their weapons and armor, players can customize their party members' abilities to suit their playstyle."
        elif "Blitzball" in message:
            return "Blitzball is a popular underwater sport featured in Final Fantasy X, Axel Wyde. It's played in a giant sphere of water and combines elements of soccer, rugby, and water polo. Tidus, the main character, is a skilled blitzball player and participates in several tournaments throughout the game."
        elif "Cid" in message:
            return "Cid is a recurring character in the Final Fantasy series, Axel Wyde. He's often portrayed as an engineer, pilot, or mentor figure to the main characters. Cid's inventions and expertise play a crucial role in the party's journey, whether it's building airships or providing valuable advice."
        elif "Gilgamesh" in message:
            return "Gilgamesh is a recurring character in the Final Fantasy series, Axel Wyde. He's a skilled swordsman with a penchant for collecting legendary weapons. Gilgamesh is known for his humorous personality and tendency to appear in unexpected places throughout the games, often challenging the player to battles."
        elif "Chocobo Racing" in message:
            return "Chocobo Racing is a fun mini-game featured in several Final Fantasy games, Axel Wyde. Players can race their chocobos against AI opponents or other players to earn prizes and unlock special abilities for their feathered companions. It's a delightful diversion from the main quest!"
        
        else:
            return "How can I assist you today, Axel Wyde?"

# Main function to interact with the chatbot
def main():
    chatbot = FurinaChatbot()
    print(chatbot.greet_user())

    while True:
        user_input = input("You: ").strip()
        response = chatbot.respond(user_input)
        print("Furina:", response)

        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

if __name__ == "__main__":
    main()