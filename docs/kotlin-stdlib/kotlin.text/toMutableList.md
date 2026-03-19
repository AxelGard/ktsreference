

# toMutableList

Returns a new MutableList filled with all characters of this char sequence.

```kotlin
fun CharSequence.toMutableList(): MutableList<Char>(source)
```

```kotlin
fun main() {
    val original = "Hello"
    val mutableList = original.toMutableList() // ['H', 'e', 'l', 'l', 'o']

    mutableList[1] = 'a' // change 'e' to 'a'
    println(mutableList.joinToString("")) // prints "Hallo"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-mutable-list.html)

    