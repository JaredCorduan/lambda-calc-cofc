# Predicate Logic

TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y
AND = lambda p: lambda q: (p)(q)(p)
OR = lambda p: lambda q: (p)(p)(q)
NOT = lambda p: (p)(FALSE)(TRUE)

to_bool = lambda b: (b)('true')('false') == 'true'

print( "\n-- predicate logic --\n")
print( "TRUE AND FALSE      ->", to_bool((AND)(TRUE)(FALSE)) )
print( "FALSE AND TRUE      ->", to_bool((AND)(FALSE)(TRUE)) )
print( "FALSE OR TRUE       ->", to_bool((OR)(FALSE)(TRUE)) )
print( "NOT (FALSE OR TRUE) ->", to_bool((NOT)(OR)(FALSE)(TRUE)) )


# Arithmetic

ZERO = lambda f: lambda x: x # the same as false :)
SUCC = lambda n: lambda f: lambda x: f((n)(f)(x))
ADD = lambda m: lambda n: lambda f: lambda x: (m)(f)((n)(f)(x))
PRED = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda u: x)(lambda u: u)
SUB = lambda m: lambda n: (n)(PRED)(m)
MULT = lambda m: lambda n: lambda f: (m)((n)(f))
ONE = (SUCC)(ZERO)
TWO = (SUCC)(ONE)
THREE = (SUCC)(TWO)
FOUR = (SUCC)(THREE)
ISZERO = lambda n: (n)(lambda x: FALSE)(TRUE)
ITE = lambda p: lambda a: lambda b: (p)(a)(b)

to_num = lambda n: n(lambda x:x+1)(0)

print( "\n-- arithmetic --\n" )
print( "ONE              ->", to_num(ONE) )
print( "TWO              ->", to_num(TWO) )
print( "TWO+THREE        ->", to_num(ADD(TWO)(THREE)) )
print( "PRED ZERO        ->", to_num(PRED(ZERO)) )
print( "PRED TWO         ->", to_num(PRED(TWO)) )
print( "FOUR-ONE         ->", to_num(SUB(FOUR)(ONE)) )
print( "ONE-FOUR         ->", to_num(SUB(ONE)(FOUR)) )
print( "TWOx(PRED THREE) ->", to_num(MULT(TWO)(PRED(THREE))) )
print( )
print( "ISZERO 0 ->", to_bool(ISZERO(ZERO)) )
print( "ISZERO 1 ->", to_bool(ISZERO(ONE)) )
print( )
print( "if (TRUE AND FALSE) then ONE else TWO ->", to_num((ITE)((AND)(TRUE)(TRUE))(ONE)(TWO)) )


# Pairs

PAIR = lambda x: lambda y: lambda f: (f)(x)(y)
FIRST  = lambda p: (p)(TRUE)
SECOND  = lambda p: (p)(FALSE)
MY_PAIR = (PAIR)(ONE)(TWO)

print( "\n-- pairs --\n" )
print( "SECOND (ONE, TWO) ->", to_num((SECOND)(MY_PAIR)) )


# Integers

NEG_ONE = (PAIR)(ONE)(TWO)
POS_FOUR = (PAIR)(FOUR)(ZERO)
INT_ADD = lambda a: lambda b: (PAIR)(ADD(FIRST(a))(FIRST(b)))(ADD(SECOND(a))(SECOND(b)))

to_int = lambda n: to_num(FIRST(n)) - to_num(SECOND(n))

print( "\n-- integers --\n" )
print( "FOUR + NEG_ONE ->", to_int(INT_ADD(POS_FOUR)(NEG_ONE)) )


# Fixed-point combinators 

# Y combinator wont work in any call-by-name language
Y = lambda g: (lambda x: g((x)(x)))(lambda x: g((x)(x)))

# But the Z combinator will!
Z = lambda g: (lambda x: g(lambda y: (x)(x)(y)))(lambda x: g(lambda y: (x)(x)(y)))

python_factorial = lambda f: lambda n: (1 if n==0 else n*f(n-1))

FACTORIAL = lambda f: lambda n: (ITE)(ISZERO(n))(ONE)(MULT(n)(f(PRED(n))))

print( "\n-- fixed-point combinators --\n" )

print( "Z combinator with python factorial of 4 ->", Z(python_factorial)(4) )

# the next will cause infinite recursion due to no short circuiting
# Z(FACTORIAL)(FOUR)

# But using python's (short circuiting) ITE:
fact_w_python_ite = lambda f: lambda n: (ONE if to_bool(ISZERO(n)) else MULT(n)(f(PRED(n))))
print( "Z combinator with python ite factorial of 4 ->", to_num(Z(fact_w_python_ite)(FOUR)) )
