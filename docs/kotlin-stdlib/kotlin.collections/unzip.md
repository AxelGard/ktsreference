

# unzip

Returns a pair of lists, where first list is built from the first values of each pair from this array, second list is built from the second values of each pair from this array.

```kotlin
fun <T, R> Array<out Pair<T, R>>.unzip(): Pair<List<T>, List<R>>(source)
```

```kotlin
fun main() {
    val pairs = arrayOf(
        1 to "one",
        2 to "two",
        3 to "three"
    )

    val (numbers, words) = pairs.unzip()

    println(numbers) // [1, 2, 3]
    println(words)   // [one, two, three]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/unzip.html)

    