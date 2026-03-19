

# constrainOnce

Returns a wrapper sequence that provides values of this sequence, but ensures it can be iterated only one time.

```kotlin
fun <T> Sequence<T>.constrainOnce(): Sequence<T>(source)
```

```kotlin
val numbers = (1..3).asSequence().constrainOnce()

// First iteration – works fine
numbers.forEach { println(it) }   // prints 1, 2, 3

// Second iteration – throws IllegalStateException
try {
    numbers.forEach { println(it) }
} catch (e: IllegalStateException) {
    println("Sequence can be iterated only once: ${e.message}")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/constrain-once.html)

    