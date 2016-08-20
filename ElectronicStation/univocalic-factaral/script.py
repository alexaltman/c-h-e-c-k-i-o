a_factaral=lambda x:(lambda:1, lambda:x*a_factaral(x-1))[x > 0]()
