
# Example

This is a example file simular to [odins demo file](https://github.com/odin-lang/Odin/blob/master/examples/demo/demo.odin).


```kotlin
/**
 * Kotlin Language Demo
 *
 * Kotlin is a modern, statically typed programming language that runs on the JVM,
 * can be compiled to JavaScript, and supports native compilation via Kotlin/Native.
 * It is fully interoperable with Java and is the preferred language for Android development.
 *
 * # Learning Kotlin
 * Official Docs       - https://kotlinlang.org/docs/home.html
 * Kotlin Playground   - https://play.kotlinlang.org/
 * Kotlin by Example   - https://play.kotlinlang.org/byExample/overview
 * Standard Library    - https://kotlinlang.org/api/latest/jvm/stdlib/
 * Kotlin Koans        - https://kotlinlang.org/docs/koans.html
 */

// ─────────────────────────────────────────────────────────────────────────────
// Top-level declarations: functions, properties, and constants can live outside
// any class at the file level.
// ─────────────────────────────────────────────────────────────────────────────

const val APP_NAME = "KotlinDemo"  // compile-time constant (must be primitive or String)
val BUILD_YEAR = 2024              // top-level read-only property (val)
var runCount = 0                   // top-level mutable property (var)

// =============================================================================
// THE BASICS
// =============================================================================

fun theBasics() {
    println("\n# The Basics")

    // -- Variables ------------------------------------------------------------
    // `val` is immutable; `var` is mutable.
    val immutable: Int = 42
    var mutable: Int = 10
    mutable += 5

    // Type inference: the compiler deduces the type from the initializer.
    val inferred = "Hello, Kotlin"   // String
    val pi       = 3.14159           // Double
    val flag     = true              // Boolean

    // Explicit numeric types
    val byteVal:   Byte   = 127
    val shortVal:  Short  = 32_000        // underscores improve readability
    val intVal:    Int    = 1_000_000
    val longVal:   Long   = 9_000_000_000L
    val floatVal:  Float  = 2.718f        // 'f' suffix required for Float literals
    val doubleVal: Double = 1.0e9

    // Characters and strings
    val ch    = 'A'
    val nl    = '\n'
    val path  = "C:\\Windows\\notepad.exe"

    // Raw (multi-line) strings use triple quotes; no escape sequences needed.
    val rawPath = """C:\Windows\notepad.exe"""
    val poem = """
        Roses are red,
        Violets are blue,
        Kotlin is great,
        And so are you.
    """.trimIndent()

    // String templates: embed expressions directly with $ or ${...}
    val name = "World"
    println("Hello, $name!")
    println("2 + 2 = ${2 + 2}")
    println("PI ~ $pi, length of poem: ${poem.length} chars")

    // -- Null Safety ----------------------------------------------------------
    // Types are non-null by default. Append '?' to allow null.
    var nonNull: String  = "always here"
    var nullable: String? = null

    // Safe-call operator: returns null instead of throwing NPE
    println(nullable?.length)   // null

    // Elvis operator: provide a default when left side is null
    val len = nullable?.length ?: 0
    println("Length or default: $len")

    // Non-null assertion: throws if null (use sparingly)
    nullable = "now non-null"
    println(nullable!!.length)

    // -- Type Checks and Casts ------------------------------------------------
    val any: Any = "I am a String"
    if (any is String) {
        // Smart cast: compiler knows `any` is String inside this block
        println("Smart-cast length: ${any.length}")
    }

    val num: Number = 3.14
    val asDouble = num as Double           // unsafe cast (throws on failure)
    val asInt    = num as? Int             // safe cast (returns null on failure)
    println("asDouble=$asDouble, asInt=$asInt")

    @Suppress("UNUSED_VARIABLE")
    val unused = listOf(immutable, mutable, inferred, flag, byteVal, shortVal,
        intVal, longVal, floatVal, doubleVal, ch, nl, path, rawPath, nonNull)
}

// =============================================================================
// CONTROL FLOW
// =============================================================================

fun controlFlow() {
    println("\n# Control Flow")

    // -- if / else as an expression -------------------------------------------
    val x = 7
    val label = if (x % 2 == 0) "even" else "odd"
    println("$x is $label")

    val clamped = if (x < 0) 0 else if (x > 10) 10 else x
    println("clamped: $clamped")

    // -- when (like a supercharged switch) ------------------------------------
    // `when` is both a statement and an expression.
    val score = 85
    val grade = when {
        score >= 90 -> "A"
        score >= 80 -> "B"
        score >= 70 -> "C"
        score >= 60 -> "D"
        else        -> "F"
    }
    println("Score $score => Grade $grade")

    // Match against a value
    val day = 3
    when (day) {
        1       -> println("Monday")
        2       -> println("Tuesday")
        3, 4    -> println("Mid-week")        // multiple values per branch
        in 5..7 -> println("End of week")     // range check
        else    -> println("Unknown day")
    }

    // `when` with type checks (replaces long if-is chains)
    fun describe(obj: Any): String = when (obj) {
        is Int     -> "Integer: $obj"
        is String  -> "String of length ${obj.length}"
        is List<*> -> "List with ${obj.size} elements"
        else       -> "Unknown: $obj"
    }
    println(describe(42))
    println(describe("hi"))
    println(describe(listOf(1, 2, 3)))

    // -- for loops ------------------------------------------------------------
    for (i in 1..5)      print("$i ")   ; println()   // inclusive range
    for (i in 1 until 5) print("$i ")   ; println()   // exclusive upper bound
    for (i in 5 downTo 1 step 2) print("$i ") ; println()  // 5 3 1

    val fruits = listOf("apple", "banana", "cherry")
    for (fruit in fruits) print("$fruit ")
    println()

    // withIndex gives both index and value
    for ((index, fruit) in fruits.withIndex()) {
        println("  [$index] $fruit")
    }

    // -- while / do-while -----------------------------------------------------
    var count = 0
    while (count < 3) { print("${count++} ") } ; println()

    var n = 3
    do { print("${n--} ") } while (n > 0) ; println()

    // -- break and continue with labels ---------------------------------------
    outer@ for (i in 1..3) {
        for (j in 1..3) {
            if (j == 2) continue@outer  // skip to next outer iteration
            print("($i,$j) ")
        }
    }
    println()

    outer2@ for (i in 1..3) {
        for (j in 1..3) {
            if (i == 2 && j == 2) break@outer2
            print("($i,$j) ")
        }
    }
    println()
}

// =============================================================================
// FUNCTIONS
// =============================================================================

fun functionsDemo() {
    println("\n# Functions")

    // -- Default and named parameters -----------------------------------------
    fun greet(name: String, greeting: String = "Hello") = println("$greeting, $name!")
    greet("Alice")
    greet("Bob", greeting = "Hi")
    greet(greeting = "Hey", name = "Carol")

    // -- Vararg ---------------------------------------------------------------
    fun sum(vararg nums: Int, initial: Int = 0): Int {
        var result = initial
        for (n in nums) result += n
        return result
    }
    println("sum() = ${sum()}")
    println("sum(1,2,3) = ${sum(1, 2, 3)}")
    println("sum(initial=10, 1,2,3) = ${sum(1, 2, 3, initial = 10)}")

    // Spread operator (*) unpacks an array into a vararg parameter
    val odds = intArrayOf(1, 3, 5)
    println("sum(*odds) = ${sum(*odds)}")

    // -- Single-expression functions ------------------------------------------
    fun square(x: Int) = x * x
    fun max(a: Int, b: Int) = if (a > b) a else b
    println("square(7) = ${square(7)}, max(3,9) = ${max(3, 9)}")

    // -- Local functions ------------------------------------------------------
    fun factorial(n: Int): Long {
        fun go(acc: Long, remaining: Int): Long =
            if (remaining <= 1) acc else go(acc * remaining, remaining - 1)
        return go(1L, n)
    }
    println("10! = ${factorial(10)}")

    // -- Higher-order functions -----------------------------------------------
    fun applyTwice(x: Int, f: (Int) -> Int) = f(f(x))
    println("applyTwice(3, ::square) = ${applyTwice(3, ::square)}")

    fun compose(f: (Int) -> Int, g: (Int) -> Int): (Int) -> Int = { x -> f(g(x)) }
    val squareThenDouble = compose({ it * 2 }, ::square)
    println("squareThenDouble(4) = ${squareThenDouble(4)}")

    // -- Extension functions --------------------------------------------------
    // Add methods to existing types without subclassing.
    fun String.isPalindrome() = this == this.reversed()
    fun Int.isPrime(): Boolean {
        if (this < 2) return false
        for (i in 2..Math.sqrt(this.toDouble()).toInt()) {
            if (this % i == 0) return false
        }
        return true
    }

    println("\"racecar\".isPalindrome() = ${"racecar".isPalindrome()}")
    println("\"kotlin\".isPalindrome()  = ${"kotlin".isPalindrome()}")
    println("17.isPrime() = ${17.isPrime()}, 18.isPrime() = ${18.isPrime()}")

    // -- Infix functions ------------------------------------------------------
    infix fun Int.pow(exp: Int): Int {
        var result = 1
        repeat(exp) { result *= this }
        return result
    }
    println("2 pow 10 = ${2 pow 10}")

    // -- Tail-recursive functions ---------------------------------------------
    // `tailrec` asks the compiler to optimize the tail call into a loop.
    tailrec fun fibTail(n: Int, a: Long = 0L, b: Long = 1L): Long =
        if (n == 0) a else fibTail(n - 1, b, a + b)
    println("fib(50) = ${fibTail(50)}")
}

// =============================================================================
// LAMBDAS AND FUNCTIONAL PROGRAMMING
// =============================================================================

fun lambdasAndFP() {
    println("\n# Lambdas and Functional Programming")

    // -- Lambda syntax --------------------------------------------------------
    val double: (Int) -> Int = { x -> x * 2 }
    val add: (Int, Int) -> Int = { a, b -> a + b }
    println("double(5) = ${double(5)}, add(3,4) = ${add(3, 4)}")

    // Single-parameter lambdas can use `it`
    val triple: (Int) -> Int = { it * 3 }
    println("triple(4) = ${triple(4)}")

    // -- Collection transformations -------------------------------------------
    val numbers = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    val evens   = numbers.filter { it % 2 == 0 }
    val squares = numbers.map { it * it }
    val total   = numbers.reduce { acc, n -> acc + n }
    val product = numbers.fold(1L) { acc, n -> acc * n }

    println("evens:   $evens")
    println("squares: $squares")
    println("sum:     $total")
    println("product: $product")

    val (evens2, odds) = numbers.partition { it % 2 == 0 }
    println("partition -> evens: $evens2, odds: $odds")

    val flattened = listOf(listOf(1, 2), listOf(3, 4), listOf(5)).flatten()
    println("flattened: $flattened")

    val words = listOf("hello world", "kotlin is great")
    val allWords = words.flatMap { it.split(" ") }
    println("flatMap words: $allWords")

    // groupBy, associateWith
    val byParity = numbers.groupBy { if (it % 2 == 0) "even" else "odd" }
    println("groupBy parity: $byParity")

    val squared = numbers.associateWith { it * it }
    println("associateWith square: $squared")

    // -- Sequences (lazy evaluation, like Java Streams) -----------------------
    // Sequences defer each step until the terminal operation, avoiding
    // the creation of intermediate lists for large data.
    val result = generateSequence(1) { it + 1 }  // infinite sequence
        .filter { it % 2 != 0 }                   // odd numbers
        .map { it * it }                           // squared
        .take(5)                                   // first 5
        .toList()
    println("First 5 odd squares (lazy): $result")

    // -- Closures -------------------------------------------------------------
    fun makeCounter(start: Int = 0): () -> Int {
        var count = start
        return { count++ }
    }
    val counter = makeCounter(10)
    println("counter: ${counter()}, ${counter()}, ${counter()}")  // 10, 11, 12
}

// =============================================================================
// CLASSES AND OBJECTS
// =============================================================================

// -- Primary constructor with property declarations ---------------------------
class Person(
    val name: String,
    var age: Int,
    private val email: String = ""
) {
    // Properties with custom getters/setters
    val isAdult: Boolean
        get() = age >= 18

    var nickname: String = name
        set(value) {
            field = value.trim()   // `field` refers to the backing field
        }

    // Secondary constructor must delegate to primary via `this(...)`
    constructor(name: String) : this(name, 0)

    // init block runs as part of the primary constructor
    init {
        require(age >= 0) { "Age must be non-negative" }
    }

    fun greet() = println("Hi, I'm $name (${if (isAdult) "adult" else "minor"})")

    // operator overloading
    operator fun compareTo(other: Person): Int = this.age.compareTo(other.age)

    override fun toString() = "Person(name=$name, age=$age)"
}

// -- Data classes -------------------------------------------------------------
// Automatically generates: equals, hashCode, toString, copy, componentN
data class Point(val x: Double, val y: Double) {
    fun distanceTo(other: Point) =
        Math.sqrt((x - other.x).let { it * it } + (y - other.y).let { it * it })
}

// -- Inheritance --------------------------------------------------------------
// Classes are `final` by default; `open` allows subclassing.
open class Shape(val color: String = "black") {
    open fun area(): Double = 0.0
    open fun describe() = println("Shape: color=$color, area=${area()}")
}

class Circle(val radius: Double, color: String = "red") : Shape(color) {
    override fun area() = Math.PI * radius * radius
    override fun describe() = println("Circle: r=$radius, area=${"%.2f".format(area())}, color=$color")
}

class Rectangle(val width: Double, val height: Double, color: String = "blue") : Shape(color) {
    override fun area() = width * height
    override fun describe() = println("Rectangle: ${width}x${height}, area=${area()}, color=$color")
}

// -- Abstract classes ---------------------------------------------------------
abstract class Animal(val name: String) {
    abstract fun sound(): String
    fun introduce() = println("I am $name and I go '${sound()}'")
}

class Dog(name: String) : Animal(name) {
    override fun sound() = "Woof"
}

class Cat(name: String) : Animal(name) {
    override fun sound() = "Meow"
}

fun classesAndObjects() {
    println("\n# Classes and Objects")

    val alice = Person("Alice", 30, "alice@example.com")
    alice.greet()
    alice.nickname = "  Ali  "
    println("nickname: '${alice.nickname}'")

    val p1 = Point(0.0, 0.0)
    val p2 = Point(3.0, 4.0)
    println("distance p1->p2: ${p1.distanceTo(p2)}")

    // `copy` with modified fields — data class feature
    val p3 = p2.copy(x = 6.0)
    println("p3 (copy of p2, x=6): $p3")

    // Destructuring via componentN functions
    val (x, y) = p2
    println("destructured: x=$x, y=$y")

    val shapes: List<Shape> = listOf(Circle(5.0), Rectangle(3.0, 4.0), Circle(1.0, "green"))
    shapes.forEach { it.describe() }
    println("Largest area: ${shapes.maxOf { it.area() }}")

    val animals = listOf(Dog("Rex"), Cat("Whiskers"), Dog("Buddy"))
    animals.forEach { it.introduce() }
}

// =============================================================================
// INTERFACES
// =============================================================================

interface Drawable {
    val strokeWidth: Int get() = 1       // property with default
    fun draw()                            // abstract
    fun drawWithBorder() {                // default implementation
        println("--- border ---")
        draw()
        println("--- border ---")
    }
}

interface Resizable {
    fun resize(factor: Double)
}

// A class can implement multiple interfaces
class Canvas(private val label: String) : Drawable, Resizable {
    private var scale = 1.0

    override fun draw() = println("Drawing '$label' at scale $scale")
    override fun resize(factor: Double) { scale *= factor }
}

fun interfacesDemo() {
    println("\n# Interfaces")
    val c = Canvas("Mona Lisa")
    c.draw()
    c.resize(2.0)
    c.drawWithBorder()
}

// =============================================================================
// SEALED CLASSES (closed type hierarchies — conceptually like Odin unions)
// =============================================================================

sealed class Result<out T> {
    data class Success<T>(val value: T)   : Result<T>()
    data class Failure(val error: String) : Result<Nothing>()
    object Loading                        : Result<Nothing>()
}

fun fetchUser(id: Int): Result<String> = when (id) {
    1    -> Result.Success("Alice")
    2    -> Result.Success("Bob")
    -1   -> Result.Loading
    else -> Result.Failure("User $id not found")
}

// Sealed classes make `when` exhaustive — the compiler warns if a branch is missing.
fun handleResult(result: Result<String>) = when (result) {
    is Result.Success -> println("Got user: ${result.value}")
    is Result.Failure -> println("Error: ${result.error}")
    Result.Loading    -> println("Loading...")
}

fun sealedClassesDemo() {
    println("\n# Sealed Classes")
    listOf(1, 2, 99, -1).map(::fetchUser).forEach(::handleResult)
}

// =============================================================================
// ENUM CLASSES
// =============================================================================

enum class Direction(val degrees: Int) {
    NORTH(0), EAST(90), SOUTH(180), WEST(270);

    fun opposite(): Direction = when (this) {
        NORTH -> SOUTH
        SOUTH -> NORTH
        EAST  -> WEST
        WEST  -> EAST
    }

    fun turnRight(): Direction = entries[(ordinal + 1) % entries.size]
}

fun enumClassesDemo() {
    println("\n# Enum Classes")
    Direction.entries.forEach { println("${it.name}: ${it.degrees} degrees") }

    val dir = Direction.NORTH
    println("Opposite of $dir: ${dir.opposite()}")
    println("Turn right from $dir: ${dir.turnRight()}")

    val d = Direction.valueOf("EAST")
    println("valueOf(\"EAST\") = $d")
}

// =============================================================================
// OBJECT DECLARATIONS AND COMPANION OBJECTS
// =============================================================================

// `object` is a singleton — instantiated lazily on first access.
object Registry {
    private val entries = mutableMapOf<String, String>()

    fun register(key: String, value: String) { entries[key] = value }
    fun lookup(key: String) = entries[key]
    override fun toString() = "Registry($entries)"
}

class Counter private constructor(initial: Int = 0) {
    var count = initial
        private set

    fun increment() { count++ }
    fun reset() { count = 0 }

    // Companion objects replace `static` members from Java.
    // They can implement interfaces and have extension functions.
    companion object Factory {
        private var instanceCount = 0

        fun create(start: Int = 0): Counter {
            instanceCount++
            return Counter(start)
        }

        fun totalCreated() = instanceCount
    }
}

fun objectsDemo() {
    println("\n# Objects and Companion Objects")

    Registry.register("lang", "Kotlin")
    Registry.register("version", "2.0")
    println(Registry)

    val c1 = Counter.create()
    val c2 = Counter.create(10)
    repeat(5) { c1.increment() }
    println("c1.count=${c1.count}, c2.count=${c2.count}")
    println("Counters created: ${Counter.totalCreated()}")

    // Object expressions create anonymous objects / ad-hoc implementations
    val clickHandler = object : Drawable {
        override fun draw() = println("Anonymous drawable drawn")
    }
    clickHandler.draw()
}

// =============================================================================
// GENERICS
// =============================================================================

// Generic class with an upper bound constraint
class Box<T : Comparable<T>>(val value: T) {
    fun isGreaterThan(other: Box<T>) = this.value > other.value
    override fun toString() = "Box($value)"
}

// Generic extension function
fun <T> List<T>.second(): T? = if (size >= 2) this[1] else null

// Reified generics: access type information at runtime (only in inline functions)
inline fun <reified T> List<*>.filterIsType(): List<T> =
    filterIsInstance<T>()

// Variance: `out` = covariant (producer), `in` = contravariant (consumer)
class Cage<out T : Animal>(private val animal: T) {
    fun getAnimal(): T = animal
}

fun genericsDemo() {
    println("\n# Generics")

    val boxA = Box(42)
    val boxB = Box(17)
    println("$boxA > $boxB ? ${boxA.isGreaterThan(boxB)}")

    val mixed: List<Any> = listOf(1, "two", 3.0, "four", 5)
    val strings = mixed.filterIsType<String>()
    println("strings from mixed list: $strings")

    // Covariance: Cage<Dog> can be assigned to Cage<Animal> because of `out`
    val dogCage: Cage<Dog> = Cage(Dog("Fido"))
    val animalCage: Cage<Animal> = dogCage
    println("animal in cage: ${animalCage.getAnimal().name}")
}

// =============================================================================
// DELEGATION
// =============================================================================

interface Logger {
    fun log(msg: String)
}

class ConsoleLogger : Logger {
    override fun log(msg: String) = println("[LOG] $msg")
}

// `by` delegates all Logger calls to the provided instance — eliminates boilerplate
class Service(logger: Logger = ConsoleLogger()) : Logger by logger {
    fun doWork() {
        log("Starting work")
        log("Work done")
    }
}

// -- Property delegation ------------------------------------------------------
class Config {
    // `lazy` initializes the value on first access (thread-safe by default)
    val heavyResource: String by lazy {
        println("  [lazy] Computing heavyResource...")
        "I was computed lazily"
    }

    // `observable` fires a callback on every assignment
    var status: String by kotlin.properties.Delegates.observable("idle") { _, old, new ->
        println("  [observable] status: $old -> $new")
    }

    // `vetoable` can reject an assignment by returning false
    var positiveOnly: Int by kotlin.properties.Delegates.vetoable(0) { _, _, new ->
        new >= 0
    }
}

fun delegationDemo() {
    println("\n# Delegation")

    val svc = Service()
    svc.doWork()

    val cfg = Config()
    println(cfg.heavyResource)   // triggers lazy init
    println(cfg.heavyResource)   // returns cached value

    cfg.status = "running"
    cfg.status = "stopped"

    cfg.positiveOnly = 5
    println("positiveOnly = ${cfg.positiveOnly}")   // 5
    cfg.positiveOnly = -1
    println("positiveOnly = ${cfg.positiveOnly}")   // still 5 — vetoed
}

// =============================================================================
// COROUTINES (structured concurrency)
// =============================================================================
// NOTE: Requires the `kotlinx-coroutines-core` dependency.

import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

fun coroutinesDemo() {
    println("\n# Coroutines")

    // -- Basic launch / async -------------------------------------------------
    runBlocking {
        // launch: fire-and-forget coroutine (returns Job)
        val job = launch {
            delay(100)
            println("Coroutine done")
        }

        // async: returns a Deferred<T> (like a Future/Promise)
        val deferred: Deferred<Int> = async {
            delay(50)
            42
        }

        println("Awaited: ${deferred.await()}")
        job.join()
    }

    // -- Flows (cold async streams, like Rx Observables) ----------------------
    fun countDown(): Flow<Int> = flow {
        for (i in 3 downTo 1) {
            delay(100)
            emit(i)
        }
    }

    runBlocking {
        countDown()
            .map { "T-$it" }
            .collect { println(it) }
    }

    // -- Channel (hot stream / CSP-style producer-consumer) -------------------
    runBlocking {
        val channel = Channel<Int>()
        launch { for (i in 1..5) { channel.send(i * i) } ; channel.close() }
        for (v in channel) print("$v ")
        println()
    }
}


// =============================================================================
// SCOPE FUNCTIONS: let, run, with, apply, also
// =============================================================================

fun scopeFunctionsDemo() {
    println("\n# Scope Functions")

    data class ServerConfig(
        var host: String = "localhost",
        var port: Int = 8080,
        var secure: Boolean = false
    )

    // `apply`: configures an object and returns the receiver itself
    val config = ServerConfig().apply {
        host   = "example.com"
        port   = 443
        secure = true
    }
    println("apply -> $config")

    // `also`: used for side-effects; returns the receiver
    val list = mutableListOf(1, 2, 3)
        .also { println("also: created list $it") }
        .also { it.add(4) }
    println("after also: $list")

    // `let`: transforms the receiver; the lambda result is returned
    val length = "Hello, Kotlin".let {
        println("let: processing '$it'")
        it.length
    }
    println("let result: $length")

    // `run`: like `let` but receiver becomes `this` inside the lambda
    val summary = config.run {
        "${if (secure) "https" else "http"}://$host:$port"
    }
    println("run -> $summary")

    // `with`: non-extension version of `run`; pass the receiver as an argument
    val info = with(config) {
        "Host=$host, Port=$port, Secure=$secure"
    }
    println("with -> $info")

    // Common idiom: null-safe block with `let`
    val maybeNull: String? = "present"
    maybeNull?.let { println("non-null value: '$it'") }
}

// =============================================================================
// COLLECTIONS IN DEPTH
// =============================================================================

fun collectionsDemo() {
    println("\n# Collections")

    // -- Immutable vs mutable -------------------------------------------------
    val immutableList = listOf(3, 1, 4, 1, 5, 9, 2, 6)
    val mutableList   = mutableListOf(3, 1, 4, 1, 5, 9, 2, 6)
    mutableList.add(5) ; mutableList.removeAt(0)

    val immutableMap  = mapOf("one" to 1, "two" to 2, "three" to 3)
    val mutableMap    = mutableMapOf("one" to 1, "two" to 2)
    mutableMap["four"] = 4

    val immutableSet  = setOf(1, 2, 2, 3, 3, 4)   // duplicates automatically removed
    val mutableSet    = mutableSetOf(1, 2, 3)
    mutableSet += 4

    println("list: $immutableList")
    println("map:  $immutableMap")
    println("set:  $immutableSet")

    // -- Sorting --------------------------------------------------------------
    println("sorted:     ${immutableList.sorted()}")
    println("sortedDesc: ${immutableList.sortedDescending()}")

    data class Employee(val name: String, val dept: String, val salary: Int)
    val employees = listOf(
        Employee("Zara", "Eng",  90_000),
        Employee("Alex", "HR",   60_000),
        Employee("Mia",  "Eng", 110_000),
        Employee("Ben",  "HR",   55_000),
    )

    // Sort by department ascending, then salary descending
    val sorted = employees.sortedWith(compareBy({ it.dept }, { -it.salary }))
    sorted.forEach { println("  ${it.dept} | ${it.name} | ${it.salary}") }

    // -- Windowing / chunking -------------------------------------------------
    val nums = (1..10).toList()
    println("chunked(3):    ${nums.chunked(3)}")
    println("windowed(4,2): ${nums.windowed(4, step = 2)}")

    // -- zip / unzip ----------------------------------------------------------
    val keys   = listOf("a", "b", "c")
    val values = listOf(1, 2, 3)
    val zipped = keys.zip(values)
    println("zipped: $zipped")
    val (ks, vs) = zipped.unzip()
    println("unzipped: $ks, $vs")
}

// =============================================================================
// DESTRUCTURING
// =============================================================================

fun destructuringDemo() {
    println("\n# Destructuring")

    // Data classes provide componentN functions automatically
    data class RGB(val r: Int, val g: Int, val b: Int)
    val (r, g, b) = RGB(255, 128, 0)
    println("r=$r, g=$g, b=$b")

    // Map entries destructure into key/value pairs
    val map = mapOf("x" to 10, "y" to 20, "z" to 30)
    for ((key, value) in map) println("  $key -> $value")

    // Lambda parameter destructuring
    val points = listOf(Point(1.0, 2.0), Point(3.0, 4.0))
    points.forEach { (x, y) -> println("  ($x, $y)") }

    // Use underscore to skip unused components
    data class Triple3(val a: Int, val b: Int, val c: Int)
    val (first, _, third) = Triple3(1, 2, 3)
    println("first=$first, third=$third")
}

// =============================================================================
// TYPE ALIASES AND INLINE VALUE CLASSES
// =============================================================================

typealias StringMap = Map<String, String>
typealias Predicate<T> = (T) -> Boolean

// Value classes wrap a single value with (usually) zero runtime overhead.
// The JVM represents them as the underlying type wherever possible.
@JvmInline
value class Metres(val amount: Double) {
    operator fun plus(other: Metres) = Metres(amount + other.amount)
    override fun toString() = "${amount}m"
}

@JvmInline
value class Seconds(val amount: Double) {
    override fun toString() = "${amount}s"
}

fun typeSystemDemo() {
    println("\n# Type Aliases and Inline Value Classes")

    val headers: StringMap = mapOf("Content-Type" to "application/json")
    println("headers: $headers")

    val isEven: Predicate<Int> = { it % 2 == 0 }
    println("isEven(4)=${isEven(4)}, isEven(5)=${isEven(5)}")

    val a = Metres(100.0)
    val b = Metres(42.5)
    println("$a + $b = ${a + b}")

    // Type safety: you cannot accidentally pass Seconds where Metres is expected
    val duration = Seconds(9.58)
    println("duration: $duration")
}

// =============================================================================
// OPERATOR OVERLOADING
// =============================================================================

data class Vector2(val x: Double, val y: Double) {
    operator fun plus(other: Vector2)  = Vector2(x + other.x, y + other.y)
    operator fun minus(other: Vector2) = Vector2(x - other.x, y - other.y)
    operator fun times(scalar: Double) = Vector2(x * scalar, y * scalar)
    operator fun unaryMinus()          = Vector2(-x, -y)
    operator fun get(index: Int) = when (index) {
        0    -> x
        1    -> y
        else -> throw IndexOutOfBoundsException("Index $index")
    }

    val magnitude get() = Math.sqrt(x * x + y * y)
    override fun toString() = "($x, $y)"
}

// Extension operators can be defined outside the class
operator fun Double.times(v: Vector2) = v * this

fun operatorOverloadingDemo() {
    println("\n# Operator Overloading")
    val a = Vector2(1.0, 2.0)
    val b = Vector2(3.0, 4.0)

    println("a=$a, b=$b")
    println("a + b = ${a + b}")
    println("a - b = ${a - b}")
    println("a * 3.0 = ${a * 3.0}")
    println("2.0 * b = ${2.0 * b}")
    println("-a = ${-a}")
    println("b[0]=${b[0]}, b[1]=${b[1]}")
    println("|b| = ${b.magnitude}")
}

// =============================================================================
// REFLECTION AND ANNOTATIONS
// =============================================================================

annotation class JsonField(val name: String = "")
annotation class Required

data class User(
    @JsonField("user_name") @Required val username: String,
    @JsonField("user_age")            val age: Int,
    val email: String     // no annotation
)

fun reflectionDemo() {
    println("\n# Reflection and Annotations")

    val kClass = User::class
    println("Class: ${kClass.simpleName}")
    println("Is data class: ${kClass.isData}")

    for (prop in kClass.memberProperties) {
        val jsonField = prop.annotations.filterIsInstance<JsonField>().firstOrNull()
        val required  = prop.annotations.filterIsInstance<Required>().firstOrNull()
        val jsonName  = if (jsonField != null && jsonField.name.isNotEmpty()) jsonField.name else prop.name
        println("  ${prop.name} -> json='$jsonName', required=${required != null}")
    }

    // Calling a constructor by reference via reflection
    val constructor = kClass.constructors.first()
    val user = constructor.call("alice", 30, "alice@example.com")
    println("Created via reflection: $user")
}

// =============================================================================
// DSL BUILDING (type-safe builders)
// =============================================================================

@DslMarker annotation class HtmlDsl

@HtmlDsl
class Tag(val name: String) {
    private val children = mutableListOf<Any>()
    private val attrs    = mutableMapOf<String, String>()

    fun attr(key: String, value: String) { attrs[key] = value }

    fun tag(name: String, block: Tag.() -> Unit): Tag {
        val child = Tag(name).also(block)
        children.add(child)
        return child
    }

    // `unaryPlus` on String allows `+"text"` syntax inside a builder block
    operator fun String.unaryPlus() { children.add(this) }

    override fun toString(): String {
        val attrStr = if (attrs.isEmpty()) "" else " " + attrs.entries.joinToString(" ") {
            "${it.key}=\"${it.value}\""
        }
        val body = children.joinToString("")
        return "<$name$attrStr>$body</$name>"
    }
}

fun html(block: Tag.() -> Unit) = Tag("html").also(block)

fun dslDemo() {
    println("\n# DSL Building (Type-Safe Builders)")

    val page = html {
        tag("head") {
            tag("title") { +"Kotlin DSL Demo" }
        }
        tag("body") {
            attr("class", "container")
            tag("h1") { +"Hello from Kotlin DSL" }
            tag("p")  { +"Type-safe HTML builders are a Kotlin superpower." }
        }
    }
    println(page)
}

// =============================================================================
// MAIN ENTRY POINT
// =============================================================================

fun main() {
    /*
     * For more Kotlin examples:
     *   Kotlin by Example   - https://play.kotlinlang.org/byExample/overview
     *   Kotlin GitHub       - https://github.com/JetBrains/kotlin
     *   Kotlin Koans        - https://kotlinlang.org/docs/koans.html
     *   Awesome Kotlin      - https://kotlin.link/
     */

    theBasics()
    controlFlow()
    functionsDemo()
    lambdasAndFP()
    classesAndObjects()
    interfacesDemo()
    sealedClassesDemo()
    enumClassesDemo()
    objectsDemo()
    genericsDemo()
    delegationDemo()
    scopeFunctionsDemo()
    collectionsDemo()
    destructuringDemo()
    typeSystemDemo()
    operatorOverloadingDemo()
    reflectionDemo()
    dslDemo()
    // coroutinesDemo()  // Uncomment if kotlinx-coroutines is on the classpath
}

```