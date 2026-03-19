

# compareTo

Compares this object with the specified object for order. Returns zero if this object is equal to the specified other object, a negative number if it's less than other, or a positive number if it's greater than other.

```kotlin
infix inline fun <T> Comparable<T>.compareTo(other: T): Int(source)
```

```kotlin
fun main() {
    val a = 5
    val b = 3
    val c = 5
    val d = 10

    // a compared to b – positive result
    println("a compareTo b: ${a compareTo b}")   // 2

    // a compared to c – equal
    println("a compareTo c: ${a compareTo c}")   // 0

    // a compared to d – negative result
    println("a compareTo d: ${a compareTo d}")   // -5
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/compare-to.html)

    