class Present
  @@all = []

  attr_reader :area, :ribbon

  def self.all
    @@all
  end

  def self.total_area
    @@all.map { |p| p.area }.reduce(0) { |total, area| total + area }
  end

  def self.total_ribbon
    @@all.map { |p| p.ribbon }.reduce(0) { |total, area| total + area }
  end

  def initialize(size_string)
    @size_string = size_string.strip
    self.parse_size
    self.calculate_area
    self.calculate_ribbon_length
    self.calculate_bow
    self.total_ribbon
    @@all << self
  end

  def to_s
    "Present> dim:#{@size_string} area:#{@area} "
  end

  def self.parse_bulk(sizes_array)
    sizes_array.each do |size|
      Present.new size
    end
  end

  def parse_size
    @size_array = @size_string.strip.split('x').map { |n| n.to_i }.sort
  end

  def calculate_area
    sa = @size_array
    @area = 2 * ((sa[0] * sa[1]) + (sa[1] * sa[2]) + (sa[2] * sa[0]))
    @area += self.calculate_shortest_side_area
  end

  def calculate_shortest_side_area
    @size_array[0] * @size_array[1]
  end

  def calculate_ribbon_length
    @ribbon = 2 * (@size_array[0] + @size_array[1]) 
  end

  def calculate_bow
    @bow = @size_array[0] * @size_array[1] * @size_array[2]
  end

  def total_ribbon
    @ribbon = @ribbon + @bow
  end
end

class Advent
  def initialize(file_location, mode='')
    @input = File.readlines('input_gh.txt')[..-2]
    self.trim_input
    if mode == 'dev'
      @data = @dev_input
    else
      @data = @input
    end
  end

  def trim_input(bound_a=0, bound_b=5)
    @dev_input = @input[bound_a..bound_b]
  end

  def solve
    Present.parse_bulk @data
  end
end

solver = Advent.new 'input_gh.txt'
solver.solve
puts Present.total_ribbon

