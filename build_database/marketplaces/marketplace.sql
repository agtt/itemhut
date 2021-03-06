-- This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

create schema marketplace;

create table marketplace.valid_markeplace (
       marketplace varchar primary key
);

insert into marketplace.valid_markeplace
       (marketplace)
values ('SAGE'),
('ASI'),
('direct');

create table marketplace.msku_sku (
       marketplace_sku varchar primary key,
       sku varchar not null,
       foreign key (sku)
               references product.sku_upc (sku)
	       on update cascade
);

create table marketplace.msku_marketplace (
       marketplace_sku varchar not null,
       marketplace varchar not null,
       primary key (marketplace_sku, marketplace),
       foreign key (marketplace_sku)
               references marketplace.msku_sku (marketplace_sku)
	       on update cascade,
       foreign key (marketplace)
               references marketplace.valid_markeplace
	       (marketplace)
	       on update cascade
);

