function fib(n::Int)
	a,b = BigInt(0), BigInt(1)
	for i in 1:n
		a,b = b,a+b
	end
	return a
end

print(fib(1000))

