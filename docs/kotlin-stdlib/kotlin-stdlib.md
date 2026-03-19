

# kotlin-stdlib

Provides a skeletal implementation of the read-only Collection interface.

```kotlin

```

```kotlin
fun main() {
    // Create an immutable list of integers
    val numbers: List<Int> = listOf(1, 2, 3, 4, 5)

    // Use collection operations provided by the standard library
    val evens = numbers.filter { it % 2 == 0 }   // Read‑only filtering
    val sum   = numbers.sum()                   // Sum of all elements

    // Output the results
    println("Numbers: $numbers")
    println("Evens:   $evens")
    println("Sum:     $sum")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/all-types.html)

    