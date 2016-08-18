# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
sys.path.append("/itemhut/pydb")
import dbconn

from models.products.kits import *

def sku_upcs():
    dbconn.cur.execute(
        """
        select sku, upc, sku_type, product_name
        from product.sku_upc
        left join product.descriptions
        using (sku);        
        """)
    a = dbconn.cur.fetchall()
    return a

def insert_sku_upc(d):
    dbconn.cur.execute(
        """
        begin;
        insert into product.sku_upc (sku, upc, sku_type)
        values (trim(%(sku)s), %(upc)s::bigint, %(sku-type)s)
        on conflict (sku)
        do update
        set upc = excluded.upc,
        sku_type = excluded.sku_type;
        commit;
        """, d)

def select_reg_products():
    dbconn.cur.execute(
        """
        select sku, upc, sku_type, product_name
        from product.sku_upc
        left join product.descriptions
        
        using (sku)
        where sku_type <> 'master';        
        """)
    a = dbconn.cur.fetchall()
    return a

def sku_types():
    dbconn.cur.execute(
        """
        select *
        from product.sku_types;
        """)
    a = dbconn.cur.fetchall()
    return a

def insert_product_descriptions(d):
    dbconn.cur.execute(
        """
        begin;
        insert into product.descriptions 
        (sku, product_name, product_description, bullet_one, 
        bullet_two, bullet_three, bullet_four, bullet_five)
        values (trim(%(sku)s), trim(%(product-name)s), 
        trim(%(product-description)s), trim(%(bullet-one)s), 
        trim(%(bullet-two)s), trim(%(bullet-three)s), 
        trim(%(bullet-four)s), trim(%(bullet-five)s))
        on conflict (sku)
        do update
        set product_name = trim(excluded.product_name),
        product_description = trim(excluded.product_description),
        bullet_one = trim(excluded.bullet_one),
        bullet_two = trim(excluded.bullet_two),
        bullet_three = trim(excluded.bullet_three),
        bullet_four = trim(excluded.bullet_four),
        bullet_five = trim(excluded.bullet_five);
        commit;
        """, d)
    
def get_upcs():
    dbconn.cur.execute(
        """
        select upc
        from product.sku_upc
        where upc is not null;
        """)
    a = dbconn.cur.fetchall()
    res = [i[0] for i in a]
    return res

def insert_new_case_box(upc, box_qty, case_qty):
    dbconn.cur.execute(
        """
        begin;
        with new_case_id (case_id) as
	     (insert into warehouse.cases (case_id)
              values (default)
	      returning case_id)
	      ,
        new_box_id (box_id) as
	      (insert into warehouse.boxes (upc, piece_qty)
	       values (%s::int, %s::int)
	       returning box_id)
        insert into warehouse.case_box (case_id, box_id, box_qty)
        select nci.case_id, nbi.box_id, %s::int
        from new_case_id nci,
        new_box_id nbi;
        commit;
        """, [upc, box_qty, case_qty])

def insert_images(d):
    dbconn.cur.execute(
        """ 
        begin; 
        insert into product.images (sku, main_image, image_one,
        image_two, image_three, image_four, image_five, image_six,
        image_seven, image_eight, image_nine, image_ten, image_eleven,
        image_twelve, swatch_image)
        values (%(sku)s, %(main-image-path)s, 
        %(image-one-path)s, %(image-two-path)s, %(image-three-path)s, 
        %(image-four-path)s, %(image-five-path)s, %(image-six-path)s,
        %(image-seven-path)s, %(image-eight-path)s, 
        %(image-nine-path)s, %(image-ten-path)s, %(image-eleven-path)s,        %(image-twelve-path)s, %(swatch-image-path)s)
        on conflict (sku)
        do update
        set main_image = trim(excluded.main_image),
        image_one = trim(excluded.image_one),
        image_two = trim(excluded.image_two),
        image_three = trim(excluded.image_three),
        image_four = trim(excluded.image_four),
        image_five = trim(excluded.image_five),
        image_six = trim(excluded.image_six),
        image_seven = trim(excluded.image_seven),
        image_eight = trim(excluded.image_eight),
        image_nine = trim(excluded.image_nine),
        image_ten = trim(excluded.image_ten),
        image_eleven = trim(excluded.image_eleven),
        image_twelve = trim(excluded.image_twelve),
        swatch_image = trim(excluded.swatch_image);
        commit;
        """, d)

def update_product_data(d):
    if d["pid"].strip() != d["sku"].strip():
        dbconn.cur.execute(
            """
            begin;
            update product.sku_upc
            set sku = trim(%(sku)s)
            where sku = trim(%(pid)s);
            commit;
            """, d)

    insert_sku_upc(d)
    insert_product_descriptions(d)

def get_sku_data(sku):
    dbconn.dcur.execute(
        """
        select sku, upc, sku_type, product_name, product_description, 
               bullet_one, bullet_two, bullet_three, bullet_four,
               bullet_five, main_image, image_one, image_two,
               image_three, image_four, image_five, image_six,
               image_six, image_seven, image_eight, image_nine,
               image_ten, image_eleven, image_twelve, swatch_image
        from product.sku_upc
        left join product.descriptions
        using (sku)
        left join product.images
        using (sku)
        where trim(sku) = trim(%s);
        """, [sku])
    a = dbconn.dcur.fetchall()
    return a
