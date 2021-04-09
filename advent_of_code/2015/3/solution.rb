require 'set'

input = File.read('./input_gh.txt')

# there are two 'drivers' now delivering packages - santa, and robo-santa
# they both have a position, but we can still assume that they're just cool with having one houses_visited slot

position = [0, 0]
houses_visited = Set.new

houses_visited << "#{position[0]}:#{position[1]}"

input.each_char do |char|
  if char == 'v'
    position[0] -= 1
  elsif char == '^'
    position[0] += 1
  elsif char == '>'
    position[1] += 1
  elsif char == '<'
    position[1] -= 1
  end
  houses_visited << "#{position[0]}:#{position[1]}"
end


p position
p houses_visited.size