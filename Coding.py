from random import randint


class  solution:
    def sortArray(self,nums):
        def quick(nums, l, r):
             if l > r:
                 return
             pos =self.partition(nums,l,r)
             self.quick(nums,0,pos-1)
             self.quick(nums,pos+1,r)

        def partition(nums,l ,r):
             i = randint(l,r)
             nums[i], nums[l] = nums[l],nums[i]
             l=l+1
             pivot = nums[l]
             pos = l
             l=l+1
             while l<=r:
                 while l<=r and nums[l]<pivot:
                       l+=1
                 while l<=r and nums[r]>pivot:
                       r-=1
                 nums[l],nums[r]=nums[r],nums[l]
                 l+=1
                 r-=1
             nums[r],nums[pos] = nums[pos],nums[r]
             return r





