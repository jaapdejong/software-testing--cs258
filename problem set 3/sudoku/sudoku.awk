###
### simple sudoku solver
###

BEGIN {
	EMPTY = ".";
}


###
### one line of the puzzle
###
{
	if (NF != 1) {
		printf("%s\n", $0);
		next;
	}

	if (SIZE == 0) {
		if      (length == 4)  VALID = "1234";
		else if (length == 9)  VALID = "123456789";
		else if (length == 16) VALID = "0123456789ABCDEF";
		else if (length == 25) VALID = "ABCDEFGHIJKLMNOPQRSTUVWXY";
		else printf("Wrong length\n");
		SIZE = length;
		QSIZE = sqrt(SIZE);
		for (y = 1; y <= SIZE; ++y) {
			for (x = 1; x <= SIZE; ++x) {
				val[x "|" y] = VALID;
			}
		}
		y = 0;
	}

	if (length != SIZE) printf("Line too short\n");
	++y;
	for (x = 1; x <= SIZE; ++x) {
		ch = substr($0, x, 1);
		if (index(VALID, ch) && !ins(x, y, ch)) printf("Bad placement\n");
	}

	if (y == SIZE) {
		ntry = 0;
		done = try(location());
		if (done) s = "OK"; else s = "### NOT SOLVED ###";
		show(" " s " [" ntry "]");
		SIZE = 0;
	}
}


###
### remove a value
### RECURSIVE
###
function del(x, y, ch, ____, id)
{
	if (length(val[x "|" y]) == 1) return val[x "|" y] != ch;
	id = index(val[x "|" y], ch);
	val[x "|" y] = substr(val[x "|" y], 1, id-1) substr(val[x "|" y], id+1);
	if (length(val[x "|" y]) == 1) return ins(x, y, val[x "|" y]);

	return 1;
}


###
### place a value
### RECURSIVE
###
function ins(x, y, ch, ____, sx, sy, nx, ny)
{
	val[x "|" y] = ch;

	for (sx = 1; sx <= SIZE; ++sx) if (sx != x && !del(sx, y, ch)) return 0;

	for (sy = 1; sy <= SIZE; ++sy) if (sy != y && !del(x, sy, ch)) return 0;

	sy = y - (y - 1) % QSIZE;
	ny = sy + QSIZE - 1;
	for (  ; sy <= ny; ++sy) {
		if (sy == y) continue;
		sx = x - (x - 1) % QSIZE;
		nx = sx + QSIZE - 1;
		for (  ; sx <= nx; ++sx) {
			if (sx != x && !del(sx, sy, ch)) return 0;
		}
	}

	return 1;
}


###
### save the whole array
###
function save(____, x, y, s)
{
	s = "";
	for (y = 1; y <= SIZE; ++y) {
		for (x = 1; x <= SIZE; ++x) {
			s = s val[x "|" y] "|";
		}
	}

	return s;
}


###
### restore the whole array
###
function restore(s, ____, x, y, id)
{
	for (y = 1; y <= SIZE; ++y) {
		for (x = 1; x <= SIZE; ++x) {
			id = index(s, "|");
			val[x "|" y] = substr(s, 1, id-1);
			s = substr(s, id+1);
		}
	}
}


###
### find empty location
###
function location(____, x, y, best, bestp, n)
{
	best = SIZE+1;
	bestp = "";

	for (y = 1; y <= SIZE; ++y) {
		for (x = 1; x <= SIZE; ++x) {
			n = length(val[x "|" y]);
			if (n == 1) continue;		# 1 = used
			if (n == 2) return x "|" y;	# 2 = optimal
			if (n < best) {			# better than previous
				best = n;
				bestp = x "|" y;
			}
		}
	}

	return bestp;
}


###
### try a location
### RECURSIVE
###
function try(p, ____, i, x, y, n, ch, s)
{
	if (p == "") return 1;

	++ntry;
	i = index(p, "|");
	x = substr(p, 1, i-1);
	y = substr(p, i+1);

	s = save();
	for (n = 1; n <= length(val[p]); ++n) {
		ch = substr(val[p], n, 1);
printf("%s", ch);
		if (ins(x, y, ch) && try(location())) return 1;
printf("\b \b");
		restore(s);
	}

	return 0;
}


###
### show the matrix
###
function show(title, ____, x, y, s, ch)
{
	if (title) printf("%s\n", title);

	s = "+";
	for (x = 1; x <= QSIZE; ++x) {
		for (y = 1; y <= QSIZE; ++y) s = s "-";
		s = s "+";
	}

	printf("%s\n", s);

	for (y = 1; y <= SIZE; ++y) {
		printf("|");
		for (x = 1; x <= SIZE; ++x) {
			ch = val[x "|" y];
			if (length(ch) != 1) ch = EMPTY;
			printf("%s", ch);
			if (x % QSIZE == 0) printf("|");
		}
		printf("\n");
		if (y % QSIZE == 0) printf("%s\n", s);
	}
}


###
### EOF
###
