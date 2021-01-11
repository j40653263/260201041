class DNA:
  def __init__(self, dna_str):
    self.dna_str = dna_str
        
    
  def count_nucleotids(self):
    counts = {"A":0, "C":0, "T":0, "G":0}
    for x in self.dna_str:
      counts[x] += 1    
    return counts
  
  def calculate_complement(self):
    replacements = {"A":"T", "T":"A", "G":"C", "C":"G"}
    reversed_dna_str = self.dna_str[::-1]
    new_dna_str = " "
      
    for x in reversed_dna_str:
      new_dna_str += replacements[x]
          
    return DNA(new_dna_str)
  
  def count_point_mutations(self, dna):
    count = 0
    for i in range(len(self.dna_str)):
      if self.dna_str[i] != dna.dna_str[i]:
        count += 1
              
    return count
  
  def find_motif(self, dna):
    lenght = len(dna.dna_str)
    locations = []
    for i in range(len(self.dna_str)):
      if self.dna_str[i:i+lenght] == dna.dna_str:
        locations.append(i)
              
    return locations
    
dna = DNA("AAA")
dna2 = DNA("TTT")
print(dna.count_nucleotids())
print(dna.calculate_complement())
print(dna.count_point_mutations(dna2))
print(dna.find_motif("TAT"))