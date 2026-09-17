#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from random import randint


class Solution:
    def sortArray(self, nums,l,r):
        if l>r:
            return
        pos = self.partition(nums,l,r)
        self.sortArray(nums,0,pos-1)
        self.sortArray(nums,pos+1,r)

    def partition(self, nums,l,r):
        i = randint(l,r)
        nums[i],nums[l] = nums[l],nums[i]
        p = nums[l]
        p_pos = l
        l=l+1
        while l<=r:

            while l<=r and nums[l]< p:
                l+=1
            while l<=r and nums[r]>p:
                r-=1
            #判断l,r是否交叉
            if l>r:
                break
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        nums[r],nums[p_pos] =nums[p_pos],nums[r]
        return r
if __name__ == '__main__':
    import boto3

    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    response = client.converse(
        modelId="us.anthropic.claude-sonnet-4-6",
        messages=[{"role": "user", "content": [{"text": "Hello"}]}],
    )

    print(response["output"]["message"]["content"][0]["text"])
