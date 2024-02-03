# https://leetcode.com/problems/maximum-product-subarray/

from itertools import groupby

class Solution(object):
    def split_on_zeroes(self, raw_list):
        split_lists = [list(group) for key, group in groupby(raw_list, key=lambda x: x == 0) if not key]
        return split_lists

    def list_product(self, product_list):
        if not len(product_list) >= 1:
            return None
        product = 1
        for elem in product_list:
            product *= elem
        return product

    def maxProduct(self, nums):
        max_products = []
        if 0 in nums:
            max_products.append(0)
        split_lists = self.split_on_zeroes(nums)
        for solo_list in split_lists:
            if not len(solo_list) >= 1:
                continue
            if len(solo_list) == 1:
                max_products.append(solo_list[0])
                continue
            negative_elements = 0
            first_negative_pos = -1
            last_negative_pos = -1
            for i in range(len(solo_list)):
                if solo_list[i] < 0:
                    negative_elements += 1
                    last_negative_pos = i
                    if first_negative_pos == -1:
                        first_negative_pos = i
            if negative_elements % 2 == 0:
                solo_list_product = self.list_product(solo_list)
                if solo_list_product is not None:
                    max_products.append(solo_list_product)
            else:
                right_sublist_product = self.list_product(solo_list[first_negative_pos+1:])
                if right_sublist_product is not None:
                    max_products.append(right_sublist_product)
                left_sublist_product = self.list_product(solo_list[:last_negative_pos])
                if left_sublist_product is not None:
                    max_products.append(left_sublist_product)
        print(max_products)
        return max(max_products)
