

# Sequence

Given an iterator function constructs a Sequence that returns values through the Iterator provided by that function. The values are evaluated lazily, and the sequence is potentially infinite.

```kotlin
inline fun <T> Sequence(crossinline iterator: () -> Iterator<T>): Sequence<T>(source)
```

```kotlin
fun main() {
    val numbers = Sequence<Int> {
        var i = 1
        val max = 10
        object : Iterator<Int> {
            override fun hasNext() = i <= max
            override fun next() = i++
        }
    }

    numbers.forEach { println(it) }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/-sequence.html)

    