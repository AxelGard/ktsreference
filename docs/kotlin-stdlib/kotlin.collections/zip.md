

# zip

Returns a list of pairs built from the elements of this array and the other array with the same index. The returned list has length of the shortest collection.

```kotlin
infix fun <T, R> Array<out T>.zip(other: Array<out R>): List<Pair<T, R>>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3)
    val letters = arrayOf("A", "B", "C")

    val zipped: List<Pair<Int, String>> = numbers zip letters

    zipped.forEach { (num, letter) ->
        println("$num -> $letter")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/zip.html)

    