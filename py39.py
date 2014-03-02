class Song(object):

	def __init__(self ,lyrics):
		print object
		print self
		print lyrics
		self.lyrics = lyrics
		print "init------------------"
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
				"I do want to get sued",
				"So I will stop right there"])

bull_on_parade = Song(['They rally around the family',
					"With pockets full of shells"])	
	
happy_bday.sing_me_a_song()

bull_on_parade.sing_me_a_song()