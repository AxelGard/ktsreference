

# iterator

Returns the given iterator itself. This allows to use an instance of iterator in a for loop.

```kotlin
inline operator fun <T> Iterator<T>.iterator(): Iterator<T>(source)
```

```kotlin
fun main() {
    val numbers = listOf(10, 20, 30)
    val iterator = numbers.iterator()   // get an Iterator<Int>

    // Thanks to the inline operator, we can use this iterator directly in a for loop
    for (value in iterator) {
        println(value)
    }
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/iterator.html)

    