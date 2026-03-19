

# generateSequence

Returns a sequence which invokes the function to calculate the next value on each iteration until the function returns null.

```kotlin
fun <T : Any> generateSequence(nextFunction: () -> T?): Sequence<T>(source)
```

```kotlin
fun main() {
    var a = 0
    var b = 1

    val fibonacci = generateSequence {
        val next = a          // current value to emit
        a = b                // advance to next pair
        b += next
        next                 // return current value
    }

    val firstTen = fibonacci.take(10).toList()
    println(firstTen)   // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/generate-sequence.html)

    